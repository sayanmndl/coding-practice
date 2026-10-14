from collections import defaultdict

'''
Inputs
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
'''

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        wordList = set(wordList)
        res = []
        layer ={}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newLayer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                    print('res', res)
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_w = w[:i]+c+w[i+1:]
                            if new_w in wordList:
                                newLayer[new_w]+= [j+[new_w] for j in layer[w]]
                                
            wordList -= set(newLayer.keys())
            layer = newLayer
            print(layer, wordList)
            
        return res