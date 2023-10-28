#!/usr/bin/env python3

""" BaseCaching module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used (LFU) caching system.
    """

    def __init__(self):
        """
        Initializes the class by calling the parent's init method and setting up usage and frequency dictionaries.
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Caches a key-value pair.

        Args:
            key: The key to be cached.
            item: The item to be associated with the key.
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == lfu]
                if len(lfu_keys) > 1:
                    lru_lfu = {k: self.usage.index(k) for k in lfu_keys}
                    discard = min(lru_lfu, key=lru_lfu.get)
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]

            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value linked to a given key, if it exists, and updates its usage and frequency.

        Args:
            key: The key whose associated value is to be retrieved.

        Returns:
            The value associated with the key if it exists; otherwise, returns None.
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None

