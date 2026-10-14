from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {} # key -> (val, freq)
        # freq -> keys ordered LRU -> MRU
        self.freq_to_keys = defaultdict(OrderedDict) 

    def _update(self, key):
        val, freq = self.key_to_val_freq[key]
        # remove current freq bucket
        del self.freq_to_keys[freq][key]

        # if current min-freq bucket became empty
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]

            if self.min_freq == freq:
                self.min_freq += 1 # freq + 1 because key is min freq now
        
        # increase freq
        self.key_to_val_freq[key] = (val, freq+1)
        # insert at end = MRU withtin this freq
        self.freq_to_keys[freq+1][key] = None


    def get(self, key):
        if key not in self.key_to_val_freq:
            return -1
        
        self._update(key)
        return self.key_to_val_freq[key][0]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            freq = self.key_to_val_freq[key][1]
            self.key_to_val_freq[key] = (value, freq)
            self._update(key)
            return
        if len(self.key_to_val_freq) == self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)

            del self.key_to_val_freq[evict_key]

            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
            