class Solution:
    def twoEditWords(self, queries, dictionary):
        ans = []
        for query in queries:
            for word in dictionary:
                diff = 0
                for a,b in zip(query, word):
                    if a != b:
                        diff+=1

                        if diff > 2:
                            break

                if diff <=2:
                    ans.append(query)
                    break
        return ans
        