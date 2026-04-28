class LinkedListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key : node

        # DLL
        self.left, self.right = LinkedListNode(0, 0), LinkedListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
    
    def remove(self, node: LinkedListNode) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node: LinkedListNode) -> None:
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        self.right.prev = prev.next = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = LinkedListNode(key, value)
            self.cache[key] = node
            self.insert(node)
        
            if len(self.cache) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
