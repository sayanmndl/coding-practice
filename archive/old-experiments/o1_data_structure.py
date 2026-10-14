class Node:

    def __init__(self, key, count):
        self.prev = None
        self.next = None
        self.count = count
        self.keys = {key} if key else set()

    def insert_after(self, new_node):
        new_node.prev = self
        new_node.next = self.next
        self.next.prev = new_node
        self.next = new_node
        return new_node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:
    def __init__(self):
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.key_to_node = {}

    def inc(self, key):
        if key not in self.key_to_node:
            if self.root.next == self.root or self.root.next.count > 1:
                new_node = Node(key, 1)
                self.key_to_node[key] = self.root.insert_after(new_node)
            else:
                self.root.next.keys.add(key)
                self.key_to_node[key] = self.root.next

        else:
            current_node = self.key_to_node[key]
            next_node = current_node.next
            new_count = current_node.count + 1

            if next_node == self.root or next_node.count > new_count:
                new_node = Node(key, new_count)
                self.key_to_node[key] = current_node.insert_after(new_node)
            else:
                next_node.keys.add(key)
                self.key_to_node[key] = next_node

            current_node.keys.discard(key)
            if not current_node.keys:
                current_node.remove()

    def dec(self, key):
        current_node = self.key_to_node[key]
        if current_node.count == 1:
            del self.key_to_node[key]
        else:
            prev_node = current_node.prev
            new_count = current_node.count - 1

            if prev_node == self.root or prev_node.count < new_count:
                new_node = Node(key, new_count)
                self.key_to_node[key] = prev_node.insert_after(new_node)
            else:
                prev_node.keys.add(key)
                self.key_to_node[key] = prev_node

        current_node.keys.discard(key)
        if not current_node.keys:
            current_node.remove()

    def getMaxKey(self):
        if self.root.prev == self.root:
            return ""
        return next(iter(self.root.prev.keys))

    def getMinKey(self):
        if self.root.next == self.root:
            return ""
        return next(iter(self.root.next.keys))
        