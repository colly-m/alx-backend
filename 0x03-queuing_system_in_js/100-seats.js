import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';


const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const queue = kue.createQueue();

const app = express();
const port = 1245;

let reservationEnabled = true;
const totalSeats = 50;

async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return seats ? parseInt(seats, 10) : 0;
}

reserveSeat(totalSeats);

app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err)

         return res.json({ status: 'Reservation failed' });
        }
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const currentSeats = await getCurrentAvailableSeats();
        if (currentSeats <= 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }

        await reserveSeat(currentSeats - 1);
        if (currentSeats - 1 === 0) {
            reservationEnabled = false;
        }
        done();
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
