from os import preadv


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.map = {}
        self.cap = capacity

        self.head = Node()
        self.tail = Node(
        )
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, node):
        next = self.head.next
        self.head.next = node
        node.next = next
        node.prev = self.head
        next.prev = node

    def _remove_node(sefl, node):
        prev, next = node.prev, node.next
        prev.next =next
        next.prev= prev

    def _move_front(self,node):
        self._remove_node(node)
        self._add_front(node)
    
    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_front(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            node = self.map[key]
            node.value = val
            self._move_front(node)

        else:
            node = Node(key, val)
            self.map[key] = node
            self._add_front(node)
            if len(self.map) > self.cap:
                lru = self._pop_tail()
                del self.map[lru.key]