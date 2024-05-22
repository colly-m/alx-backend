#!/usr/bin/python3
"""Module to create aclass to inherit from a caching system"""
import heapq
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class to inherit and implement a LFU cache system"""

    def __init__(self) -> None:
        """Initializes the class"""
        super().__init__()
        self.cache_list = {}
        self.cache_order = []

    def put(self, key, item):
        """
        Function to add item into cache
        key: str - The key represent the item value
        item: any - The item to be stored in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_list[key] += 1
                self.cache_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_frequency = float('inf')
                least_frequency_keys = []
                for lru_key in self.cache_order:
                    if self.cache_list[lru_key] < least_frequency:
                        least_frequency = self.cache_list[lru_key]
                        least_frequency_keys = [lru_key]
                    elif self.cache_list[lru_key] == least_frequency:
                        least_frequency_keys.append(lru_key)
                del_key = least_frequency_keys.pop(0)
                del self.cache_data[del_key]
                del self.cache_list[del_key]
                self.cache_order.remove(del_key)
                print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item
            self.cache_list[key] = 1
            self.cache_order.insert(0, key)

    def get(self, key):
        """
        Get an item by key
        key: str - The param to retrieve the corresponding item
        """
        if key is not None and key in self.cache_data:
            self.cache_list[key] += 1
            self.cache_order.remove(key)
            self.cache_order.insert(0, key)
            return self.cache_data[key]
        else:
            return None
