#!/usr/bin/python3
"""Module to create a class MRUCache to inherit from a caching system"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class to inherit from BaseCaching and is a caching system"""
    def __init__(self):
        """FUnction to initialize the MRUCache class"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """
        Function to add an item into the cache
        key: str - The param to represent the item to add
        item: any - The param to e added
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.mru = key
                else:
                    # discard the most recently used item
                    discarded = self.mru
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
                    self.cache_data[key] = item
                    self.mru = key
            else:
                self.cache_data[key] = item
                self.mru = key

    def get(self, key):
        """
        Function to get an item by the key
        key: str - The param to get the item y
        """
        if key is not None and key in self.cache_data:
            self.mru = key
            return self.cache_data[key]
        else:
            return None
