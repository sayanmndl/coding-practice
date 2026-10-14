class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def findRoot(self, tree):
        root_val = 0

        for node in tree:
            root_val ^= node.val

            for child in node.children:
                root_val^=child.val

        # every non-root val appears twice and cancels out
        # root_val is not the root's value.
        for node in tree:
            if node.val == root_val:
                return node
        
        return None


    def findRoot1(self, tree):
        children = set()
        for node in tree:
            for child in node.children:
                children.add(child)

        for node in tree:
            if node not in children:
                return node
        return None
