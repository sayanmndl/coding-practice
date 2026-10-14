
from re import X


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = set()

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.freq = {} # sentence -> freq
        self.prefix = "" # curr input state
        self.curr = self.root

        for sentence, count in zip(sentences, times):
            self.freq[sentence] = self.freq.get(sentence, 0)+count
            self._insert(sentence)

    def _insert(self, sentence):
        node = self.root

        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

            node.sentences.add(sentence)

    def input(self, c):
        if c == '#': # end of sentence
            self.freq[self.prefix] = self.freq.get(self.prefix, 0)+1
            self._insert(self.prefix)
            self.prefix = "" # reset prefix for next query
            self.curr = self.root
            return []
        self.prefix += c

        # if prefix doesnt exist in trie
        if self.curr is None or c not in self.curr.children:
            self.curr = None
            return []
        
        self.curr = self.curr.children[c]
        candidates = self.curr.sentences

        ranked = sorted(candidates, key = lambda sentence: (-self.freq[sentence], sentence))
        return ranked[:3]