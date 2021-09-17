from collections import OrderedDict
class LRUCache:
    def __init__(self,capacity):
        self.cache=OrderedDict()
        self.capacity=capacity
    def put(self,key,value):
        self.cache[key]=value # first, we add / update the key.
        self.cache.move_to_end(key) #move the key to the end to show that it was most recently used.
        '''  But here we will also check whether the length of our
             ordered dictionary has exceeded our capacity,
             If so we remove the first key (least recently used)
        '''
        if(len(self.cache) > self.capacity):
            self.cache.popitem(last = False)
        
    def get(self,key):
        if(len(self.cache)!=0):
            if(key not in self.cache):
                return -1
            else:
                self.cache.move_to_end(key)
                return self.cache[key]
cache=LRUCache(2)
print(cache.cache)
cache.put(1,1)
print(cache.cache)
cache.put(2,2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(3,3)
print(cache.cache)
cache.get(3)
print(cache.cache)


'''
Output:

OrderedDict()
OrderedDict([(1, 1)])
OrderedDict([(1, 1), (2, 2)])
OrderedDict([(2, 2), (1, 1)])
OrderedDict([(1, 1), (2, 2)])
OrderedDict([(2, 2), (3, 3)])
OrderedDict([(2, 2), (3, 3)])
'''
