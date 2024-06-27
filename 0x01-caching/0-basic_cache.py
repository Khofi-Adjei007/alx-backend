#!/usr/bin/env python3

'''Task 0: Basic dictionary caching system
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache class that inherits from
    BaseCaching and provides a simple caching system.
    '''

    def put(self, key, item):
        '''Adds an item to the cache with the given key.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Retrieves the value from the cache for the given key.
        '''
        return self.cache_data.get(key)
