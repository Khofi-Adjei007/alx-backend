#!/usr/bin/env python3

'''Task 1: FIFO caching system
'''

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFOCache class that inherits from BaseCaching
    and implements a FIFO caching system.
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds an item to the cache with the given
        key using FIFO eviction policy.
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''Retrieves the value from the cache for the given key.
        '''
        return self.cache_data.get(key)
