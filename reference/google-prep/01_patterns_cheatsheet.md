# Patterns Cheat Sheet: Interview Day

> Read this the morning of the interview. Every template here was run against small asserts before it went in. Python, 45 minutes, no autocomplete, no execution.

---

## 0. Interview flow (45 min)

| Min | Step | What you do | Say out loud |
|---|---|---|---|
| 0–5 | **Clarify** | Input size, types, ranges, duplicates, negatives, empty input, sorted?, output format, ties | "Before I start, can I check a few things: how big can n get? Can values be negative? What should I return if there's no answer?" |
| 5–8 | **Examples** | Work one normal case and one edge case by hand | "Let me run a small example so I'm sure I've got the problem right: for `[2,1,5]` I'd expect `…`." |
| 8–12 | **Brute force** | State it, give its complexity, don't code it | "The naive way is to try every pair, which is O(n²). That works, but n is 1e5, so I want O(n log n) or better." |
| 12–17 | **Optimize** | Name the pattern, state the invariant, get a nod | "Sums are monotone in the window, so a sliding window works. The invariant is that the window always holds at most k distinct values. Does that sound reasonable before I code it?" |
| 17–35 | **Code** | Clean names, small helpers, narrate as you go | "I'll write a helper `ok(cap)` for feasibility, then binary search on the answer." |
| 35–40 | **Test** | Trace the example line by line, then the edge cases | "Tracing `[2,1,5]`: lo=0, hi=2… Edge cases: empty, a single element, all equal, all negative." |
| 40–45 | **Complexity + follow-ups** | Time, space, and why | "O(n log n) time for the sort, O(n) space for the map. If the input streams, I'd…" |

**Rules of thumb**
- Never go quiet for more than about 60 seconds. Thinking out loud is the signal they're scoring.
- If you get stuck: shrink the input (n=1, 2, 3), look for monotonicity, ask "what if it were sorted?", or ask "what would I precompute?"
- When you spot a bug, say so: "I see an off-by-one here, so I'll fix it." Catching your own bugs scores well.
- Declare your invariants (loop invariant, window invariant, stack invariant). Google interviewers listen for them.
- Common follow-ups: streaming input (use a heap, a window, or reservoir sampling), data that doesn't fit in memory (external sort, chunking, hashing into shards), many queries (precompute: prefix sums, sparse table, trie).

---

## 1. Sliding window
**Cue:** contiguous subarray or substring + "longest / shortest / count" + a constraint that stays valid as the window shrinks → window.
```python
def longest_at_most_k_distinct(s, k):          # variable window
    cnt, lo, best = Counter(), 0, 0
    for hi, c in enumerate(s):
        cnt[c] += 1
        while len(cnt) > k:                     # shrink until valid
            cnt[s[lo]] -= 1
            if cnt[s[lo]] == 0: del cnt[s[lo]]
            lo += 1
        best = max(best, hi - lo + 1)
    return best
# fixed size k: s += a[i] - a[i-k]
```
**"Exactly K" trick:** `exactly(k) = atMost(k) - atMost(k-1)`. In `atMost`, add `hi - lo + 1` per step, which counts the subarrays ending at `hi`.
**O(n)** time, O(alphabet) space.
**Traps:** (1) Negative numbers break the "shrink when the sum is too big" logic, so use prefix sums + a hashmap or a deque instead. (2) Forgetting to `del` a zero count leaves `len(cnt)` wrong. (3) Updating `best` inside the shrink loop when you meant to update it after.

## 2. Two pointers
**Cue:** a sorted array (or one you can sort), pair/triplet sums, palindromes, in-place partitioning, or merging two sorted arrays.
```python
def three_sum(a):
    a.sort(); res = []
    for i in range(len(a) - 2):
        if i and a[i] == a[i - 1]: continue        # skip dup anchors
        j, k = i + 1, len(a) - 1
        while j < k:
            s = a[i] + a[j] + a[k]
            if s < 0: j += 1
            elif s > 0: k -= 1
            else:
                res.append((a[i], a[j], a[k])); j += 1
                while j < k and a[j] == a[j - 1]: j += 1
    return res
```
**O(n²)** for 3-sum, O(n) for a pair. Fast/slow pointers handle cycle detection (Floyd) and finding a list's midpoint.
**Traps:** (1) Sorting loses the original indices, so carry `(val, idx)` if you need to return indices. (2) Dedupe at both levels. (3) `i < j` vs `i <= j`: decide whether the two pointers may share an element.

## 3. Prefix sums + hashmap
**Cue:** "subarray sum equals / divisible by K", negative numbers allowed, many range-sum queries, or "longest subarray with equal 0s and 1s" (map 0 to -1).
```python
def subarray_sum_k(a, k):
    seen, s, res = {0: 1}, 0, 0              # {prefix: count}; seed 0!
    for x in a:
        s += x
        res += seen.get(s - k, 0)
        seen[s] = seen.get(s, 0) + 1
    return res
```
**O(n)** time and space. For the *longest* subarray, store the first index of each prefix (`{0: -1}`) and never overwrite it. For divisibility, key on `s % k`. Python's `%` is already non-negative.
**Traps:** (1) Forgetting the `{0: 1}` seed. (2) Updating `seen` before the lookup, which counts the empty subarray. (3) 2D range queries need `P[i+1][j+1] = a + P[i][j+1] + P[i+1][j] - P[i][j]`.

## 4. Binary search
**Cue:** sorted input, "minimize the max / maximize the min", "smallest X such that…", a monotone yes/no predicate, or an O(log n) requirement.
```python
def first_true(lo, hi, ok):     # invariant: answer in [lo, hi]; hi = "none" sentinel
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid): hi = mid    # mid might be the answer, so keep it
        else: lo = mid + 1      # mid is definitely not
    return lo
# search on the answer: ship_capacity -> first_true(max(w), sum(w), feasible)
```
**Rotated array:** one half is always sorted. If `a[lo] <= a[mid]`, the left half is sorted: check whether `a[lo] <= t < a[mid]` and recurse into that side, otherwise go to the other. For the minimum, compare against `a[hi]`: if `a[mid] > a[hi]` then `lo = mid+1`, else `hi = mid`.
**O(log n)**, or O(n log range) when searching on the answer.
**Traps:** (1) An infinite loop from `lo = mid` when mid rounds down. With `lo = mid` you must use `mid = (lo+hi+1)//2`. (2) Mixing up `while lo < hi` with `lo <= hi` (the second is for exact-match search with `mid±1`). (3) Searching the answer with the wrong bounds, e.g. the low bound must be `max(w)`, not 0. For "last true", search for the first false and subtract 1.

## 5. Monotonic stack / deque
**Cue:** "next greater/smaller element", "how far until…", histogram area, stock span, sliding-window max/min.
```python
def next_greater(a):                      # stack holds indices; values decreasing
    res, st = [-1] * len(a), []
    for i, x in enumerate(a):
        while st and a[st[-1]] < x:
            res[st.pop()] = x
        st.append(i)
    return res

def window_max(a, k):                     # deque holds indices; values decreasing
    dq, res = deque(), []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] <= x: dq.pop()
        dq.append(i)
        if dq[0] <= i - k: dq.popleft()   # expired
        if i >= k - 1: res.append(a[dq[0]])
    return res
```
**O(n)** amortized, since each index is pushed and popped once.
**Traps:** (1) Storing values when you need indices for widths or distances. (2) Strict vs. non-strict comparison changes how duplicates are handled. For "sum of subarray minimums", use `<` on one side and `<=` on the other. (3) In largest-rectangle, forgetting the sentinel `0` that flushes the stack: `for i, x in enumerate(h + [0])`, with width `i - (st[-1]+1 if st else 0)`.

## 6. Heaps
**Cue:** "k largest/smallest/closest", "merge k sorted", a running median, a scheduler where you always take the next best item, or a stream.
```python
def top_k(a, k):                          # min-heap of size k -> O(n log k)
    h = []
    for x in a:
        heapq.heappush(h, x)
        if len(h) > k: heapq.heappop(h)
    return sorted(h, reverse=True)

def merge_k(lists):                       # (val, list_id, idx); id breaks ties
    h = [(l[0], i, 0) for i, l in enumerate(lists) if l]; heapq.heapify(h); out = []
    while h:
        v, i, j = heapq.heappop(h); out.append(v)
        if j + 1 < len(lists[i]): heapq.heappush(h, (lists[i][j+1], i, j+1))
    return out
```
**Two heaps (median):** `lo` is a max-heap (store negated values) and `hi` is a min-heap. Push to `lo`, move `lo`'s top to `hi`, then rebalance so `len(lo) >= len(hi)`.
**Traps:** (1) Pushing uncomparable objects: tuples with equal first fields fall through to comparing nodes, so add an index tiebreaker. (2) Forgetting to negate for a max-heap, and forgetting to negate back. (3) "Top k" needs a **min**-heap of size k (and vice versa). Mention quickselect for an O(n) average.

## 7. Intervals / sweep line
**Cue:** meetings, booking, "minimum rooms", "merge overlapping", "points covered by most intervals", skyline.
```python
def merge_intervals(iv):
    out = []
    for s, e in sorted(iv):
        if out and s <= out[-1][1]: out[-1][1] = max(out[-1][1], e)
        else: out.append([s, e])
    return out

def max_overlap(iv):                      # half-open [s, e): end(-1) sorts before start(+1)
    ev = sorted([(s, 1) for s, _ in iv] + [(e, -1) for _, e in iv])
    cur = best = 0
    for _, d in ev: cur += d; best = max(best, cur)
    return best
```
**O(n log n).** Alternatives: a min-heap of end times for meeting rooms, and sorting by end time for greedy selection (see §14).
**Traps:** (1) Touching endpoints `[1,2],[2,3]`: settle whether they overlap with the interviewer, then pick `<` vs `<=` and the event tiebreak order. (2) `max(out[-1][1], e)`, because a contained interval mustn't shrink the end. (3) Mutating the input. Copy it or say you're doing it on purpose.

## 8. BFS / DFS / topological sort
**Cue:** grid or graph reachability, "minimum steps" with unweighted edges (BFS), counting components or flood fill (DFS), "prerequisites/order/dependencies" (topo sort).
```python
def topo(n, edges):                                   # Kahn's algorithm
    adj, indeg = defaultdict(list), [0] * n
    for u, v in edges: adj[u].append(v); indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0); order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
    return order if len(order) == n else []           # [] => cycle
```
Grid BFS: `deque([src])` and `dist = {src: 0}`. For each of the 4 neighbors, bounds-check, wall-check, and **mark visited when you enqueue**. For multi-source BFS, put all sources in the queue at the start. DFS cycle detection in a directed graph uses three colors (white/gray/black): reaching a gray node means a cycle.
**O(V + E).**
**Traps:** (1) Marking visited on dequeue, which enqueues duplicates and blows up the runtime. (2) Recursive DFS on a 1e5-node path hits the recursion limit, so use an explicit stack. (3) An undirected cycle check must skip the parent edge (or just use union-find).

## 9. Dijkstra / 0-1 BFS
**Cue:** shortest path with **non-negative** weights. Use 0-1 BFS when weights are only 0 or 1 (e.g. "minimum walls to break" or "minimum direction flips"). With state such as `(node, fuel)` or `(node, keys_mask)`, run Dijkstra or BFS over the expanded state space.
```python
def dijkstra(adj, src):
    dist = {src: 0}; pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue                      # stale entry
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd; heapq.heappush(pq, (nd, v))
    return dist
# 0-1 BFS: deque; on relax, appendleft if w == 0 else append
```
**O((V+E) log V)**. 0-1 BFS is O(V+E).
**Traps:** (1) Skipping the stale-entry check, which is still correct but slow. (2) Negative edges break Dijkstra, so use Bellman-Ford (or SPFA). (3) "At most K stops" means the state must include the stop count, or use Bellman-Ford run K+1 times on a copy of `dist`.

## 10. Union-find
**Cue:** dynamic connectivity, "are x and y connected", counting components as edges arrive, redundant edges, grouping by equivalence (accounts merge, similar strings), Kruskal's MST.
```python
class DSU:
    def __init__(self, n): self.p, self.r = list(range(n)), [0] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]   # path halving
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False                          # already joined => cycle edge
        if self.r[a] < self.r[b]: a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]: self.r[a] += 1
        return True
```
**~O(α(n))** per operation.
**Traps:** (1) `self.p[a] = b` on the raw nodes instead of their roots. (2) Non-integer keys: map them to ids, or use a dict with `setdefault(x, x)`. (3) It can't handle deletions, so process the operations in reverse (offline) instead.

## 11. Trie
**Cue:** prefix queries, autocomplete, word search over a grid with many words, longest common prefix, max XOR pair (a binary trie).
```python
class Trie:
    def __init__(self): self.root = {}
    def insert(self, w):
        node = self.root
        for c in w: node = node.setdefault(c, {})
        node['$'] = True                     # end-of-word marker
    def _walk(self, s):
        node = self.root
        for c in s:
            if c not in node: return None
            node = node[c]
        return node
    def search(self, w): n = self._walk(w); return bool(n and '$' in n)
    def starts_with(self, p): return self._walk(p) is not None
```
**O(L)** per operation, O(total characters) space.
**Traps:** (1) Confusing "prefix exists" with "word exists" (the `$` marker). (2) In Word Search II, failing to prune found words or dead branches, which TLEs. (3) Memory: talk about a dict vs. a 26-slot array, and about storing the word at its terminal node.

## 12. Backtracking
**Cue:** "all combinations / permutations / subsets / partitions", constraint satisfaction (N-Queens, Sudoku), small n (≤ 15–20).
```python
def subsets_with_dup(a):
    a.sort(); res, path = [], []
    def bt(i):
        res.append(path[:])                           # copy!
        for j in range(i, len(a)):
            if j > i and a[j] == a[j - 1]: continue   # dedupe at same depth
            path.append(a[j])                         # choose
            bt(j + 1)                                 # explore (j: reuse allowed)
            path.pop()                                # unchoose
    bt(0); return res
```
**Pruning:** sort, then `break` once a candidate exceeds the remaining target. For permutations, track a `used[]` array. With duplicates, also skip `a[i]==a[i-1] and not used[i-1]`.
**O(2^n · n)** for subsets, **O(n! · n)** for permutations.
**Traps:** (1) `res.append(path)` without a copy, which leaves every result as the same empty list. (2) Dedupe with `j > i`, not `j > 0`. (3) Recursing with `j+1` vs `j` vs `i+1`: decide whether reuse is allowed and whether order matters.

## 13. Dynamic programming
**Cue:** "number of ways", "min/max cost", "is it possible", choices whose subproblems overlap, or greedy fails on a counterexample.
**Define the state:** write "`dp[i]` = the answer for the prefix `a[:i]` / the suffix starting at i / ending exactly at i", then list the **choices** at that state. That gives the recurrence. Then the base cases, the iteration order, and where the answer lives.
```python
def rob(a):                                   # 1D: dp[i] = max(dp[i-1], dp[i-2]+a[i])
    prev, cur = 0, 0
    for x in a: prev, cur = cur, max(cur, prev + x)
    return cur

def lcs(s, t):                                # 2D over two strings
    m, n = len(s), len(t); dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = 1 + dp[i+1][j+1] if s[i] == t[j] else max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

def knapsack01(wt, val, W):
    dp = [0] * (W + 1)
    for w, v in zip(wt, val):
        for c in range(W, w - 1, -1):         # REVERSE => each item once
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[W]                              # unbounded (coin change): loop FORWARD
```
```python
def lis(a):                                   # O(n log n) patience
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)      # bisect_right for non-decreasing
        if i == len(tails): tails.append(x)
        else: tails[i] = x
    return len(tails)

def burst_balloons(nums):                     # interval DP: by increasing length
    a = [1] + nums + [1]; n = len(a); dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):         # k = LAST balloon burst in (i, j)
                dp[i][j] = max(dp[i][j], dp[i][k] + a[i]*a[k]*a[j] + dp[k][j])
    return dp[0][n - 1]

def tsp(d):                                   # bitmask DP, n <= ~16
    n = len(d)
    @cache
    def f(mask, u):
        if mask == (1 << n) - 1: return d[u][0]
        return min(d[u][v] + f(mask | 1 << v, v) for v in range(n) if not mask >> v & 1)
    return f(1, 0)
```
**Memo vs. tabulation:** write the top-down `@cache` version first, because it's fastest to get right and it naturally skips unreachable states. Switch to bottom-up when recursion depth exceeds about 1e4 or when you need space optimization. **Space optimization:** if row `i` only reads row `i+1`, keep two rows (or one, with the right loop direction). Complexity = #states × cost per transition.
**Traps:** (1) Wrong loop direction in 1D knapsack: forward means unbounded, reverse means 0/1. (2) In counting problems, combinations need the coins loop on the outside and permutations need the amount loop on the outside. (3) Initializing to 0 when "impossible" should be `inf`/`-inf`, and returning `inf` instead of -1.

## 14. Greedy (and how to justify it)
**Cue:** "max number of non-overlapping…", "min arrows/platforms/jumps", sort-then-scan, and a locally best choice that never needs undoing.
```python
def max_non_overlapping(iv):            # activity selection: sort by END
    end, cnt = float('-inf'), 0
    for s, e in sorted(iv, key=lambda x: x[1]):
        if s >= end: cnt += 1; end = e
    return cnt
```
**Exchange argument (say this):** "Take any optimal solution O. If its first choice isn't the greedy choice g, swap g in. g ends no later, so everything after it in O is still compatible and the count doesn't drop. Repeat, and O becomes the greedy solution, so greedy is optimal."
**Traps:** (1) Sorting by start or length instead of end time. (2) Not trying a quick counterexample: if a 3-element case breaks greedy, switch to DP. (3) Stating the greedy choice without any justification.

## 15. Bit tricks
**Cue:** "appears once/twice", subsets of n ≤ 20, state compression, powers of two, XOR properties.
```python
x & (x - 1)        # clear lowest set bit; x>0 and x&(x-1)==0 -> power of 2
x & -x             # isolate lowest set bit (Fenwick trees)
bin(x).count('1')  # popcount (x.bit_count() on 3.10+)
reduce(xor, a)     # single number: pairs cancel
for m in range(1 << n): [a[i] for i in range(n) if m >> i & 1]   # all subsets
s = m
while s: ...; s = (s - 1) & m                                      # all submasks of m
```
**Traps:** (1) Precedence: `mask >> i & 1` works, but `x & 1 == 0` parses as `x & (1 == 0)`, so add parentheses. (2) Python ints are unbounded, so `~x` is `-x-1`. Mask with `& 0xFFFFFFFF` to emulate 32-bit. (3) Iterating submasks over all masks costs O(3^n), not 4^n.

---

## Python gotchas
- **Recursion limit is about 1000.** `sys.setrecursionlimit(10**6)` helps, but deep recursion can still crash the C stack. For depth ≥ 1e4, say "I'd convert this to an iterative stack."
- **`heapq` is a min-heap only.** For a max-heap, push `-x`. `heapq.nlargest(k, a)` exists. There's no decrease-key, so push again and skip stale entries.
- **`bisect`:** `bisect_left(a, x)` is the first index with `a[i] >= x`, and `bisect_right` is the first with `a[i] > x`. Count of x = `right - left`. Python 3.10+ adds a `key=` argument.
- **`collections`:** `deque` (O(1) at both ends; `list.pop(0)` is O(n)), `defaultdict(list)`, `Counter` (`most_common(k)`, `c1 - c2` drops non-positive counts), `OrderedDict.move_to_end` for LRU.
- **`functools.cache` / `lru_cache(None)`:** arguments must be hashable, so convert lists to tuples. A cache inside a method leaks between test cases, so define it inside the function or call `f.cache_clear()`.
- **Mutable default args:** `def f(a, seen=[])` shares one list across calls. Use `seen=None`.
- **Grid aliasing:** `[[0]*n]*m` makes m references to the same row. Use `[[0]*n for _ in range(m)]`.
- **Misc:** `//` floors toward −inf (`-7//2 == -4`), so use `int(a/b)` to truncate toward zero. `float('inf')` is fine for comparisons. Strings are immutable, so build a list and join it.

## Constraints → target complexity

| n up to | Acceptable | Typical approach |
|---|---|---|
| ≤ 10 | O(n!) | permutations, brute-force backtracking |
| ≤ 20 | O(2^n · n) | subsets, bitmask DP |
| ≤ 100 | O(n³) | Floyd-Warshall, interval DP |
| ≤ 1,000 | O(n²) | 2D DP, all pairs |
| ≤ 1e5 | O(n log n) | sort, heap, binary search, segment tree |
| ≤ 1e6 | O(n) | two pointers, sliding window, prefix sums, hashing |
| ≥ 1e9 | O(log n) / O(1) | binary search on the answer, math |

Python: roughly 1e7 simple operations per second.
