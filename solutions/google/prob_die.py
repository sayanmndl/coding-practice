class Solution:
    def probabilityAWin(self, a, b):
        j = 0
        wins = 0

        for x in a:
            # move j until b[j] >= x
            # b[0:j] are smaller than x
            while j < len(b) and b[j] < x:
                j+=1
            
            wins += j
        total = len(a) + len(b)

        return wins/total