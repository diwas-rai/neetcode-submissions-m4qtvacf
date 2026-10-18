class DLLNode:
    def __init__(self, key=-1, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.left, self.right = DLLNode(), DLLNode()
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.left, self.left.next

        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next, nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        node = self.store[key]

        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        
        self.store[key] = DLLNode(key, value)
        self.insert(self.store[key])
        if len(self.store) > self.cap:
            print(key, value, self.store[key].key)
            lru = self.right.prev
            self.remove(lru)
            del self.store[lru.key]
