class Solution:
    def canTransform(self, start, end):
        n = len(start)
        i,j = 0,0

        while True:
            # skip all 'X' characters in start string
            while i<n and start[i]=='X':
                i+=1
            
            # skip all 'X' in end string
            while j<n and end[j]=='X':
                j+=1
            
            # both pointers have reached the end
            if i >=n and j>=n:
                return True

            # one reached the end but not other -> impossible
            # the non-X chars dont match
            if i>=n or j>=n or start[i]!=end[j]:
                return False

            # 'L' can only move left so start[i] = l and i<j is invalid
            if start[i] == 'L' and i<j:
                return False

            #'R' can only move right so start[i]  = R and i> j is invalid
            if start[j] == 'R' and i>j:
                return False

            i+=1
            j+=1
