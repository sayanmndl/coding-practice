from collections import deque

def ladderLength(beginWord, endWord, wordList):

    if endWord not in wordList:
        return 0

    word_set = set(wordList)
    charlist = set([c for word in word_set for c in word])
    queue = deque([(beginWord, 1)])
    visited = set([beginWord])

    while queue:
        word, length = queue.popleft()

        if word == endWord:
            return length

        for i in range(len(word)):
            for c in charlist:
                if c == word[i]:
                    continue
                newword = word[:i]+c+word[i+1:]
                if newword in word_set and newword not in visited:
                    visited.add(newword)
                    queue.append((newword, length+1))
    return 0