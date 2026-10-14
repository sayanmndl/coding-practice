
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9+7
        k = r-l+1

        if n == 1:
            return k
        
        up = [0]*k
        down = [0]*k

        for j in range(k):
            up[j] = j
            down[j] = k-1-j

        for _ in range(3, n+1):
            new_up = [0]*k
            new_down = [0]*k            
            
            prefix = 0
            for j in range(k):
                new_up[j] = prefix
                prefix = (prefix+down[j])%MOD
            
            suffix = 0
            for j in range(k-1,-1,-1):
                new_down[j] = suffix
                suffix = (suffix+up[j])%MOD
            up,down = new_up, new_down
        return (sum(up)+sum(down))%MOD

        