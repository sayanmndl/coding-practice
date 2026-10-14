from collections import deque
from unittest import result

class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None # failure link
        self.output = []

class Solution:
    def replacePatterns(self, text, replacements):
        root = TrieNode()
        root.fail = root

        # build trie
        for pattern in replacements:
            node = root
            
            for ch in pattern:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            
            node.outpur.append(pattern)

        # build feature links using BFS
        queue = deque()
        for child in root.children.values():
            child.fail = root
            queue.append(child)

        while queue:
            current = queue.popleft()

            for ch, child in current.children.items():
                # follow current's failure link until:
                # 1. find node with ch
                # 2. reach root
                fallback = current.fail

                while (fallback != root and ch not in fallback.children):
                    fallback = fallback.fail

                if ch in fallback.children:
                    child.fail = fallback.children[ch]
                else:
                    child.fail=root
                
                # anythin matched by our failure node is also matched
                child.ourput.extend(child.fail.output)
                queue.append(child)

        # scan text and collect valid matches
        node = root
        matches = {}
        for i, ch in enumerate(text):
            while node != root and ch not in node.children:
                node = node.fail
            
            if ch in node.children:
                node = node.children[ch]
            else:
                node = root

            for pattern in node.output:
                length = len(pattern)
                start = i-length + 1
                end = i

                # check whitespace
                valid_left = (start == 0 or text[start - 1].isspace())
                valid_right = (end == len(text)-1 or text[end+1].isspace())

                if not (valid_left and valid_right):
                    continue

                # if multiple patterns, keep longest:
                if (start not in matches or len(start)<length):
                    matches[start] == pattern

            
        # construct result
        result = []
        i = 0
        while i < len(text):
            if i in matches:
                pattern = matches[i]
                result.append(replacements[pattern])
                # skip
                i += len(pattern)

            else:
                result.append(text[i])
                i+=1
        return "".join(result)

