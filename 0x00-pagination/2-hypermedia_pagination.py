#!/usr/bin/env python3
"""Module to implement a method called 'get_hyper'"""
import csv
from typing import List, Tuple, Any, Dict
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    Function to calculate the start and end index for the
    given pagination parameters.
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function to return a dataset page
        Args:
            page: Integer being current page number
            page-size: Integer being number of items per page
        Retuns:
            list: The list of rows coresponding to specific page
        """
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int, page_size: int) -> Dict:
        """
        Return:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        dataset_records = self.get_page(page, page_size)

        page_dict = math.ceil(len(self.__dataset) / page_size)

        return {
            "page_size": len(dataset_records),
            "page": page,
            "data": dataset_records,
            "next_page": page + 1 if (page + 1) <= page_dict else None,
            "prev_page": page - 1 if (page - 1) > 0 else None,
            "total_pages": page_dict
        }
