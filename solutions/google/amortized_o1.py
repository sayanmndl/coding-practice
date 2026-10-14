class Node:
    def __init__(self, key = None, count = 0):
        self.count = count
        self.keys = {key} if key else set()
        self.prev = None
        self.next = None

    def insert_after(self, new_node: "Node"):
        new_node.prev = self
        new_node.next = self.next
        self.next.prev = new_node
        self.next = new_node
        return new_node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOOne:
    def __init__(self):
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.key_to_node = {}

    def inc(self, key):
        if key not in self.key_to_node:
            if self.root.next == self.root or self.root.next.count > 1: # empty list or no count 1 node exists
                new_node = Node(key, 1)
                self.key_to_node[key] = self.root.insert_after(new_node)
            else:
                self.root.next.keys.add(key)
                self.key_to_node[key] = self.root.next

        else: # key exists 
            curr_node = self.key_to_node[key]
            next_node = curr_node.next
            new_count = curr_node.count + 1

            if next_node == self.root or next_node.count > new_count: # end of list or new count node is not available
                new_node = Node(key, new_count)
                self.key_to_node[key] = curr_node.insert_after(new_node)
            else:
                next_node.keys.add(key)
                self.key_to_node[key] = next_node

            curr_node.keys.discard(key)
            if not curr_node.keys:
                curr_node.remove()

    def dec(self, key):
        if key not in self.key_to_node:
            raise ValueError('Key not found, check again')
        
        curr_node = self.key_to_node[key]
        if curr_node.count == 1:
            del self.key_to_node[key]
        else:
            prev_node = curr_node.prev
            new_count = curr_node.count - 1

            if prev_node == self.root or prev_node.count < new_count: # 1 item in list or node with count doesnt exist
                new_node = Node(key, new_count)
                self.key_to_node[key] = prev_node.insert_after(new_node)
            else:
                prev_node.keys.add(key)
                self.key_to_node[key] = prev_node
        
        curr_node.keys.discard(key)
        if not curr_node.keys:
            curr_node.remove()

    
    def getMaxKey(self):
        if self.root.prev == self.root:
            return ""
        return next(iter(self.root.prev.keys))


    def getMinKey(self):
        if self.root.next == self.root:
            return ""
        return next(iter(self.root.next.keys))


ds = AllOOne()

ds.inc("hello")
print(ds.getMaxKey())   # hello
print(ds.getMinKey())   # hello

ds.inc("hello")
print(ds.getMaxKey())   # hello
print(ds.getMinKey())   # hello

ds.inc("leet")
print(ds.getMaxKey())   # hello
print(ds.getMinKey())   # leet

ds.inc("leet")
print(ds.getMaxKey())   # hello OR leet
print(ds.getMinKey())   # hello OR leet

ds.inc("leet")
print(ds.getMaxKey())   # leet
print(ds.getMinKey())   # hello

ds.dec("leet")
print(ds.getMaxKey())   # hello OR leet
print(ds.getMinKey())   # hello OR leet

ds.dec("hello")
print(ds.getMaxKey())   # leet
print(ds.getMinKey())   # hello

ds.dec("hello")
print(ds.getMaxKey())   # leet
print(ds.getMinKey())   # leet