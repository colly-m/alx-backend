#!/usr/bin/python3
"""Module to create a class that inherits from a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class to inherit from BaseCaching and implements a basic caching
    system"""

    def put(self, key, item):
        """
        Function that adds an item into the cache
        key: str - The key to associate with the item
        item: any -  Item to be stored in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Function to get an item by key
        key: str - The key to retrieve the item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
