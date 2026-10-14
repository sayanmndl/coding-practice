class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr_node = self.root
        
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_end_of_word = True

    def search(self, word):
        
        def dfs_search(word_substring, node):
            for i in range(len(word_substring)):
                char = word_substring[i]
                if char == '.':
                    for child_node in node.children.values():
                        if child_node is not None:
                            if dfs_search(word_substring[i+1:], child_node):
                                return True

                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            
            return node.is_end_of_word

        return dfs_search(word, self.root)