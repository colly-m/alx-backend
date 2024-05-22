#!/usr/bin/python3
"""Module to create a class LIFOCache to inherit from a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class to inherit BaseCaching and implements a LIFO cache"""

    def __init__(self):
        """initializes a LIFOCache class"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Function to add item into the cache
        key: str - the key to represent the item
        item; any - the parameter to be stored into cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            self.cache_data[key] = item
            self.cache_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_order.pop(-2)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        Function to get item by key
        key: str - param to get the item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
