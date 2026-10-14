from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [[(-1,0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        h = self.history[index]
        
        if h[-1][0] == self.snap_id:
            h[-1] = (self.snap_id, val)
        else:
            h.append((self.snap_id, val))

    def snap(self) -> int:
        result = self.snap_id
        self.snap_id+=1
        return result
        

    def get(self, index: int, snap_id: int) -> int:
        h = self.history[index]
        pos = bisect_right(h, (snap_id, float('inf')))
        return h[pos-1][1]
        