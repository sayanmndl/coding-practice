from typing import List

class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1

        # total covered x-lenght for each node
        self.tree = [0] * (4 * self.n)

        # number of rectangles fully covering this nodes's interval
        self.count = [0] * (4 * self.n)

    def update(self, node, l, r, ql, qr, delta):
        if ql>r or qr<l: # no overlap
            return 

        # complete overlap
        if ql >= l and r <= qr:
            self.count[node] += delta
            self._pull(node, l, r)
            return

        mid = (l+r)//2

        self.update(node*2, l, mid, ql, qr, delta)
        self.update(node*2+1, mid+1, r, ql, qr, delta)
        self._pull(node,l,r)


    def _pull(self, node, l, r):
        # if this entire segment is covered by >= 1 active square
        # its union lenght is simply its full geometric lenght
        if self.count[node] > 0:
            self.tree[node] = self.xs[r+1] - self.xs[l]
        # leaf with no coverage
        elif l == r:
            self.tree[node] = 0

        # otherewise combine childrens covered lengths
        else:
            self.tree[node] = (self.tree[node*2] + self.tree[node*2+1])

    def covered_length(self):
        return self.tree[1]

class Solution:
    def seperateSquares(self, squares):
        events = []
        xs = []

        for x, y, side in squares:
            x2 = x+side
            y2 = y+side

            # bottom edge active
            events.append((y, +1, x, x2))
            # top edge, inactive
            events.append((y2, -1, x, x2))
            xs.append(x)
            xs.append(x2)

        # coordinate compression
        xs = sorted(set(xs))
        index = {x:i for i,x in enumerate(xs)}
        events.sort()
        tree = SegmentTree(xs)
        strips = []
        total_area = 0
        
        i = 0
        prev_y = events[0][0]

        # sweep upward
        while i < len(events):
            curr_y = events[i][0]

            # before proceesing event as curr y, tree contains all squares between prev_y and curr_y
            if curr_y > prev_y:
                width = tree.covered_length()
                height = curr_y - prev_y
                area = width * height
                strips.append((prev_y, curr_y, width))
                total_area+=area

            while i < len(events) and events[i][0] == curr_y:
                _, delta, x1, x2 = events[i]
                left = index[x1]
                right = index[x2] - 1
                tree.update(1,0,tree.n-1, left, right, delta)

            prev_y = curr_y
        
        # find the y coordinate containing half the area
        target = total_area/2
        area_below = 0
        for y1, y2, width in strips:
            if area_below == target:
                return float(y1)

            strip_area = width * (y2 - y1)
            if area_below + strip_area >= target:
                needed = target - area_below
                return y1+needed/width
            
            area_below += strip_area
        
        return float(strips[-1][1])
