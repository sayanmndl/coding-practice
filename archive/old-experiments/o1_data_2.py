class Node:
    def __init__(self, key = None, count = 0):
        self.keys = {key} if key else set(        )
        self.count = count
        self.next = None
        self.prev = None
    
    def insert_after(self, new_node):
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
        self.keys_to_node = {}

    def inc(self, key):
        if key not in self.keys_to_node:
            if self.root.next == self.root or self.root.next.count > 1: # empty list or next count > 1
                new_node = Node(key, 1)
                self.keys_to_node[key] = self.root.insert_after(new_node)
            else: # list non empty and count 1 present
                self.root.next.keys.add(key)
                self.keys_to_node[key] = self.root.next

        else: # key in keys to node dict
            curr_node = self.keys_to_node[key]
            next_node = curr_node.next
            new_count = curr_node.count + 1
            if next_node == self.root or next_node.count > new_count: # end of list or next node count is higher than next count
                new_node = Node(key, new_count)
                self.keys_to_node[key] = curr_node.insert_after(new_node)
            else: # next count exists in list
                next_node.keys.add(key)
                self.keys_to_node[key] = next_node
            
            curr_node.keys.discard(key) # no more needed - remove
            if not curr_node.keys:
                curr_node.remove()

    def dec(self, key):
        if key not in self.keys_to_node:
            return

        curr_node = self.keys_to_node[key]
        if curr_node.count == 1: # only count 1
            del self.keys_to_node[key]
        else:
            prev_node = curr_node.prev
            new_count = curr_node.count - 1
            if prev_node == self.root or prev_node.count < new_count: # start of list or node DNE
                new_node = Node(key, new_count)
                self.keys_to_node[key] = prev_node.insert_after(new_node)
            else: # count node exists
                prev_node.keys.add(key)
                self.keys_to_node[key] = prev_node

        curr_node.keys.discard(key) # final cleanup
        if not curr_node.keys:
            curr_node.remove()

    def getMaxKey(self):
        if self.root.prev == self.root: # empty
            return ""
        return next(iter(self.root.prev.keys)) # return from end of list

    def getMinKey(self):
        if self.root.next == self.root:
            return ""
        return next(iter(self.root.next.keys)) # return from start of list
        