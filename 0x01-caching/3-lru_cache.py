#!/usr/bin/python3
"""Module to Create a class LRUCache to inherit from a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A class that inherits from BaseCaching and implements a LRU caching system.
    """

    def __init__(self):
        """
        Initialize the LRUCache class.
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Function to add an item into the cache
        key: str - The param to represent the item.
        item: any - The item to be stored in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_recently_used_key = self.cache_order.pop(0)
                del self.cache_data[least_recently_used_key]
                print("DISCARD: {}".format(least_recently_used_key))
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """
        Function to get an item by key
        key: str - The param to get the corresponding item
        """
        if key is not None and key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.append(key)
            return self.cache_data[key]
        else:
            return None
