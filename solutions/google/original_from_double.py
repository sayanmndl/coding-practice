from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)

        if n%2 != 0:
            return []

        count = Counter(changed)
        original = []
        changed.sort()

        for num in changed:
            if count[num] == 0:
                continue
            if count[2*num]==0:
                return []
            original.append(num)
            count[num]-=1
            count[2*num]-=1
        return original