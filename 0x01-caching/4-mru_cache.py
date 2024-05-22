#!/usr/bin/python3
"""Module to create a class MRUCache to inherit from a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class to inherit from BaseCaching and is a caching system"""
    def __init__(self):
        """FUnction to initialize the MRUCache class"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Function to add an item into the cache
        key: str - The param to represent the item to add
        item: any - The param to e added
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recently_used_key = self.cache_order[-1]
                del self.cache_data[most_recently_used_key]
                self.cache_order.pop()
                print("DISCARD: {}".format(most_recently_used_key))
            self.cache_data[key] = item
            self.cache_order.insert(0, key)

    def get(self, key):
        """
        Function to get an item by the key
        key: str - The param to get the item y
        """
        if key is not None and key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.insert(0, key)
            return self.cache_data[key]
        else:
            return None
