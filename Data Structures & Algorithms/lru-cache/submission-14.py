class LinkedListNode:
    def __init__(self, val=0, key=None, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev


class DLL:
    def __init__(self):
        self.left_guard, self.right_guard = LinkedListNode(), LinkedListNode()
        self.left_guard.next = self.right_guard
        self.right_guard.prev = self.left_guard

    def insert(self, node):
        prev, nxt = self.right_guard.prev, self.right_guard
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.dll = DLL()
        self.capacity = capacity
        self.cache = {}  # key : node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.dll.remove(node)
        self.dll.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dll.remove(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = LinkedListNode(value, key)
        self.dll.insert(self.cache[key])

        while len(self.cache) > self.capacity:
            lru = self.dll.left_guard.next
            self.dll.remove(lru)
            del self.cache[lru.key]
