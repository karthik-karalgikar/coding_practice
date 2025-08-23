class Cache():
    def __init__(self, evictionPolicy, storage):
        self.evictionPolicy = evictionPolicy
        self.storage = storage

    def put(self, key, value):
        if self.storage.contains(key):
            self.storage.add(key, value)
            self.evictionPolicy.keyAccessed(key)

            return
        
        if self.storage.is_full():
            victim = self.evictionPolicy.evictKey()
            if victim is not None:
                self.storage.remove(victim)

        self.storage.add(key, value)
        self.evictionPolicy.keyAccessed(key, is_new = True)

    def get(self, key):
        value = self.storage.get(key)
        if value is not None:
            self.evictionPolicy.keyAccessed(key)
        
        return value

class Storage():
    def __init__(self, capacity):
        self.data = {}
        self.capacity = capacity

    def size(self):
        return len(self.data)
    
    def is_full(self):
        return self.size() >= self.capacity

    def add(self, key, value):
        self.data[key] = value       

    def remove(self, key):
        self.data.pop(key, None)

    def get(self, key):
        return self.data.get(key)
    
    def contains(self, key):
        return key in self.data

class EvictionPolicy():
    def __init__(self, dll, mapper: dict):
        self.dll = dll
        self.mapper = mapper #(Hashmap)

    def keyAccessed(self, key, is_new = False):
        if key in self.mapper:
            self.dll.move_to_end(self.mapper[key])
        elif is_new:
            node = DLLNode(key)
            self.mapper[key] = node
            self.dll.add_node_at_end(node)
    
    def evictKey(self):
        node = self.dll.pop_lru()
        if not node:
            return None
        key = node.key
        self.mapper.pop(key, None)
        return key
    
class DLL():
    def __init__(self):
        self.head = DLLNode(None)
        self.tail = DLLNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_before(self, ref_node, node):
        node.prev = ref_node.prev
        node.next = ref_node
        ref_node.prev.next = node
        ref_node.prev = node
        self.size = self.size + 1

    def add_node_at_end(self, node):
        self.insert_before(self.tail, node)

    def detach_node(self, node):
        if node is self.head or node is self.tail:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size = self.size - 1

    def move_to_end(self, node):
        self.detach_node(node)
        self.add_node_at_end(node)

    def pop_lru(self):
        if self.size == 0:
            return None
        lru = self.head.next
        self.detach_node(lru)

        return lru

class DLLNode():
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

dll = DLL()
mapper = {}
policy = EvictionPolicy(dll, mapper)
store = Storage(capacity=2)
cache = Cache(policy, store)

cache.put("1", 101)  
cache.put("2", 102)
cache.put("3", 103)  
cache.get("2")      
cache.put("4", 104)   

print(cache.get("1"))  
print(cache.get("2")) 
print(cache.get("4"))


'''
TRACING :
What does cache exacty do? 
It holds the data temporarily for faster access and when it's storage is full, it removes some of the data to make 
space for nee data.
And which data needs to be removed is decided by various policies like 
1. Least Recently Used - LRU
2. Least Frequently Used - LFU
3. First In First Out - FIFO
4. Last in First Out - LIFO

So, to design a cache we basically need a storage class and an evictionPolicy class, and of course, a Cache class.

What is Cache supposed to do?
It gets and puts values. 
so the functions would be 
get(key)
put(key, value)

But we design storage first, because only if storage exists we can get and put values in the cache. 

And for it to not traverse every element stored, to achieve O(1) time complexity, we use Mapper(HashMap) for storage, 
and an integer value for capacity.

Storage is supposed to add, remove and get data. 
It is also supposed to check if the storage is full and if it contains the key that is being accessed.

so the behaviours for these would be:
1. def add(key, value)
2. def remove(key)
3. def get(key)
4. def is_full()
5. def contains(key)

Now, moving on to Eviction Policy:
This is supposed to see the key which is accessed and evict the key from storage. 

So the behaviours for this would be:
1. def keyAccessed(key)
2. def evictKey()

The behaviours are the same irrespective of the eviction algorithm we have chosen.

We can use Doubly Linked List for storing data and since we are using Mapper, the key value pair is stored and it 
is easier to access an element. 

We make another class called DLLNode(), which defines the node 
self.key = key
self.head = None
self.tail = None

This defines the node and is empty as of now. 

Now, to create the different functions the DLL is supposed to handle, we create a DLL() class:

self.head = DLLNode(None)
self.tail = DLLNode(None)
self.head.next = self.tail
self.tail.prev = self.head
self.size = 0

(Currently there are no nodes in the DLL)

to insert elements/nodes to the DLL, we create insert behaviour(function)

def insert_before(ref_node, node):
    node.prev = ref_node.prev
    node.next = ref_node
    ref_node.prev.next = node
    ref_node.prev = node
    self.size = self.size + 1

    Supppose there is a DLL 
    1 <-> 2 <-> 3 

    and suppose 2 is accessed, so the procedure should be
    2 is detached
    1 is connected to 3
    2 is added at the end so that it becomes the most recently used. 

    so according to this function, ref_node is 2, node is 3
    node.prev = ref_node.prev
    3.prev = 2.prev => 3.prev = 1
    node.next = ref_node
    3.next = 2
    ref_node.prev.next = node
    2.prev.next => 1.next = 3
    ref_node.prev = node
    2.prev = 3

    so now, the DLL is 
    1 <-> 3 <-> 2

This function is only about inserting. But we have to make different functions like 
adding the node to the end
detaching a node
moving the node to the end
popping the LRU node(which is the first node)

Moving on to the last class, Cache

we call the different functions here from storage and evictionPolicy
'''