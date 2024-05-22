#!/usr/bin/python3
"""Module to create a class to FIFO inherit from a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class to inherit and implement a FIFO cachesystem"""

    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Function to add item into cache
        key: str - The key represent the item value
        item: any - The item to be stored in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            self.cache_data[key] = item
            self.cache_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        Function to get an item by key
        key: str - The key to get corresponding item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
