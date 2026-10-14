
from typing import List

class Solution:
    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        INF = float('inf')

        best = [INF] * (numLaps + 1)

        for f,r in tires:
            lap_time = f
            total = 0
            k = 1

            while k <= numLaps and lap_time <= changeTime+f:
                total+= lap_time
                best[k] = min(best[k], total)
                lap_time*=r
                k+=1

        dp = [INF]*(numLaps+1)
        dp[0] = -changeTime

        for i in range(1, numLaps+1):
            for k in range(1,i+1):
                if best[k] == INF:
                    break

                dp[i] = min(dp[i], dp[i-k]+changeTime+best[k])
        return dp[numLaps]