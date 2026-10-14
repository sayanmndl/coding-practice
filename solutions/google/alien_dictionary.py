from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        # every char should be in graph even if theres no edges
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}

        # build precedence
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            min_len = min(len(word1), len(word2))

            # invalid prefix: 'abc' vs 'ab'
            if (len(word1) > len(word2) and word1[:min_len]==word2[:min_len]):
                return ""

            # find first differing char
            for j in range(min_len):
                if word1[j] != word2[j]:
                    u = word1[j]
                    v = word2[j]

                    # void counting duplicate edge
                    if v not in graph[u]:
                        graph[u].add(v)
                        indegree[v]+= 1
                    # only frist different
                    break
            
            # kahn's topological sort
            queue = deque(
                char for char in indegree
                if indegree[char] == 0
            )

            order = []
            while queue:
                char = queue.popleft()
                order.append(char)

                for neigh in graph[char]:
                    indegree[neigh] -= 1
                    
                    if indegree[neigh] == 0:
                        queue.append(neigh)

            # if not every char was processed, there was cycle
            if len(order) != len(indegree):
                return ""

            return "".join(order) 
