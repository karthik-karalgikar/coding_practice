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

cache.put("1", 101)   # MRU: a
cache.put("2", 102)
cache.put("3", 103)  
cache.get("2")      
cache.put("4", 104)   # full; evict LRU (b), keep a; insert c (order: a, c)

print(cache.get("1"))  # -> None (evicted)
print(cache.get("2"))  # -> 1
print(cache.get("4"))