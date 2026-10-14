# Tier 2 — DP variants & sorting from scratch

Four Tier 2 problems: **LC 174** Dungeon Game (reverse grid DP), **LC 2188** Minimum Time to Finish the Race (precompute stints + 1D DP, reportedly Google-original in flavour), **LC 3699** Number of ZigZag Arrays I (DP + prefix sums), and **LC 912** Sort an Array (merge sort + 3-way randomized quicksort, with heap sort as a follow-up).
Each solution was tested in a scratch file with fixed asserts plus randomized checks against a brute force.

## 1. LC 174 — Dungeon Game (reverse grid DP) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** A knight starts at the top-left of an `m×n` grid and must reach the princess at the bottom-right, moving only right or down. Each cell adds its value to his HP, and values can be negative. If HP ever drops to ≤ 0, he dies. Return the minimum starting HP.
Example: `[[-2,-3,3],[-5,-10,1],[10,30,-5]]` → `7` (path R→R→D→D).

**Clarify:** Does the start cell count? (yes). Must HP be ≥ 1 at every moment, including at the end? (yes). Is the grid non-empty? (yes, m,n ≥ 1). Is the answer bounded by int? (yes).

**Approach:** Brute force: enumerate all C(m+n−2, m−1) paths, track each one's min prefix sum, and answer `max(1, 1 − minPrefix)` minimized over paths. That's exponential.
**Why forward DP fails:** a forward state needs two numbers, the current HP and the minimum HP needed so far, and they trade off. One path might need less starting HP but arrive with almost nothing, while another needs more but arrives rich, and which is better depends on the cells *ahead*. So there's no single optimal-substructure value going forward.
**Key insight:** go backward. `need[i][j]` = min HP on entering `(i,j)` to survive to the end. The future is fully summarized by one number.
Recurrence: `need[i][j] = max(1, min(need[i+1][j], need[i][j+1]) − d[i][j])`, with a sentinel of `1` just past the princess. **O(mn) time, O(n) space** with a rolling row.
```python
def calculate_minimum_hp(dungeon: List[List[int]]) -> int:   # O(mn) time, O(n) space
    m, n = len(dungeon), len(dungeon[0])
    INF = float('inf')
    need = [INF] * (n + 1)      # need[j]: min HP to enter (i, j) and survive to the end
    need[n - 1] = 1             # sentinel: after the princess you need 1 HP
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            best_next = min(need[j], need[j + 1])
            need[j] = max(1, best_next - dungeon[i][j])
        need[n] = INF
    return need[0]
```
**Dry run:** Bottom row (right to left): `-5` → need 6, `30` → max(1, 6−30)=1, `10` → 1. Middle row: `1` → max(1, 6−1)=5, `-10` → min(5,1)+10=11, `-5` → min(11,1)+5=6. Top row: `3` → max(1,5−3)=2, `-3` → min(2,11)+3=5, `-2` → min(5,6)+2=**7**. ✓
**Edge cases & tests:**
- A single cell: `[[0]]`→1, `[[-5]]`→6, `[[100]]`→1 (HP is always ≥ 1).
- A single row or column: `[[0,0,0,-10]]`→11, `[[-1],[-1],[5]]`→3.
- A big positive cell can't "bank" HP against an earlier deficit, which is exactly what the `max(1, ·)` captures.
- `assert calculate_minimum_hp([[-2,-3,3],[-5,-10,1],[10,30,-5]]) == 7`; plus 500 random grids up to 4×4 checked against brute-force path enumeration.

**Follow-ups:**
- *Also return the path?* Keep the full `need` table, then walk forward from (0,0), always stepping to the neighbour with the smaller `need`.
- *Can he also move up or left?* Then it's no longer a DAG. Binary search on the starting HP, with a feasibility check by BFS/Dijkstra that maximizes HP (feasible if the max-HP path stays > 0). That's O(mn log(mn) · log V).
- *Alternative to the reverse DP:* binary search on the answer plus a forward "max HP reachable while staying > 0" DP. It works, but the reverse DP is cleaner.

**Pattern hook:** when the constraint depends on the *future* (staying ≥ 1 all the way to the end), run the DP from the goal backward so each state is a single number.

## 2. LC 2188 — Minimum Time to Finish the Race (precompute + 1D DP) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** `tires[i] = [f, r]`: on a fresh tire, the x-th consecutive lap takes `f·r^(x−1)` seconds. You can switch to any fresh tire (unlimited supply of each) at a cost of `changeTime`. Return the minimum time to finish `numLaps` laps.
Example: `tires=[[2,3],[3,4]], changeTime=5, numLaps=4` → `21` (2+6, change 5, 2+6).

**Clarify:** Can I reuse the same tire type after changing? (yes, it's a fresh copy). Can r be 1? (yes, constraints say r ≥ 1, which matters for the loop bound). Sizes? (T ≤ 1e5, numLaps ≤ 1000, f, r, changeTime ≤ 1e5). Is the first tire free? (yes, there's no change cost at the start).

**Approach:** Brute force: at each lap, choose to change or continue, and which tire, which is exponential.
**Key insight 1:** split the race into *stints*. The tire identity only matters within a stint, so precompute `best[k]` = the cheapest k straight laps on any single tire. **Key insight 2:** a stint never needs to run past the point where the next lap costs ≥ `changeTime + f`, since a fresh tire would be at least as good. With r ≥ 2 that means at most ~18 laps (2^17 > 2e5). The r = 1 tires never degrade, so only the cheapest one matters.
Recurrence: `dp[i] = min over k of dp[i−k] + changeTime + best[k]`, with `dp[0] = −changeTime`. **O(T·18 + numLaps·K) time**, where K is the longest useful stint. **O(numLaps) space.**
```python
def minimum_finish_time(tires: List[List[int]], change_time: int, num_laps: int) -> int:
    # O(T log(changeTime) + numLaps * K) time, K = longest useful stint (<= ~18 when r >= 2)
    INF = float('inf')
    best = [INF] * (num_laps + 1)        # best[k]: min time for k straight laps on one tire
    ones = [f for f, r in tires if r == 1]
    useful = [(f, r) for f, r in tires if r > 1] + ([(min(ones), 1)] if ones else [])
    for f, r in useful:                  # r == 1 tires: only the cheapest one matters
        lap, total = f, 0
        for k in range(1, num_laps + 1):
            total += lap
            best[k] = min(best[k], total)
            if lap * r >= change_time + f:   # next lap costs >= a fresh tire: stop
                break
            lap *= r
    dp = [INF] * (num_laps + 1)          # dp[i]: min time to finish i laps
    dp[0] = -change_time                 # the first stint pays no change time
    for i in range(1, num_laps + 1):
        for k in range(1, i + 1):
            if best[k] == INF:
                break                    # best[] is finite on a prefix only
            dp[i] = min(dp[i], dp[i - k] + change_time + best[k])
    return dp[num_laps]
```
**Dry run:** Tire [2,3] gives laps 2, 6, 18. It stops after lap 2 (18 ≥ 5+2), so best[1]=2 and best[2]=8. Tire [3,4] gives best[1]=min(2,3)=2.
dp: dp0=−5, dp1=2, dp2=min(2+7, −5+13)=8, dp3=min(8+7, 2+13)=15, dp4=min(15+7, 8+13)=**21**. ✓
**Edge cases & tests:**
- `[[1,10],[2,2],[3,4]], 6, 5` → 25 (LC example 2).
- `numLaps=1` → min f. `changeTime=0` → numLaps·min f.
- An r=1 tire: `[[5,1]],1000,10` → 50 (one long stint, so the loop must not be capped at 18).
- `[[1,100000]],100000,4` → 2·(1+1e5)+1e5. Overflow-safe in Python because the loop stops before lap blows up.
- Plus 400 random cases (including r=1 tires) checked against a memoized brute force over every stint/tire choice. Perf: 2e5 tires with numLaps=1000 runs in under 1s.

**Follow-ups:**
- *Why the `dp[0] = −changeTime` trick?* It lets every stint uniformly add `changeTime`. The alternative is to special-case k = i.
- *What if each tire type has limited stock?* Then the state needs the counts used, so it becomes knapsack-like and much harder. Clarify the stock before designing.
- *Is best[k] monotone?* No, so the DP must try every k ≤ K. It doesn't satisfy the convexity needed for faster convolution tricks.

**Pattern hook:** "segments, each with its own internal cost, plus a fixed cost per break" means: precompute the best segment cost by length, then run a 1D partition DP.

## 3. LC 3699 — Number of ZigZag Arrays I (DP + prefix sums) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** Given `n, l, r`, count arrays of length `n` with every value in `[l, r]` such that adjacent values differ and no three consecutive elements are strictly increasing or strictly decreasing. In other words, the steps strictly alternate up/down. Return the count mod 1e9+7.
Example: `n=3, l=4, r=5` → `2` ([4,5,4], [5,4,5]). Example: `n=3, l=1, r=3` → `10`.
*Assumption:* this is the statement as I understand LC 3699 (n ≤ 2000, r−l ≤ 2000). Only `k = r−l+1` matters, not the actual values.

**Clarify:** Does n=1 count every single value? (yes, k arrays). Are equal neighbours forbidden? (yes). Can the first step be up or down? (either). Modulus? (1e9+7).

**Approach:** Brute force: enumerate all kⁿ arrays and check each, O(kⁿ·n).
DP: `up[v]` = arrays ending at value v whose last step went up, and `down[v]` likewise for down. An up step must follow a down step:
`up'[v] = Σ_{u<v} down[u]`, `down'[v] = Σ_{u>v} up[u]`.
Naively that's O(n·k²). **Key insight:** each transition is a prefix (or suffix) sum, so a running total makes it **O(n·k) time and O(k) space**. Base case (length 2): `up[v] = v`, `down[v] = k−1−v`.
```python
MOD = 10**9 + 7
def zigzag_arrays(n: int, l: int, r: int) -> int:   # O(n*k) time, O(k) space, k = r-l+1
    k = r - l + 1
    if n == 1: return k % MOD
    up = list(range(k))                  # up[v]: length-2 arrays ending at v with last step UP
    down = [k - 1 - v for v in range(k)] # down[v]: ... last step DOWN
    for _ in range(n - 2):
        # new_up[v] = sum(down[u] for u < v); new_down[v] = sum(up[u] for u > v)
        new_up, new_down = [0] * k, [0] * k
        run = 0
        for v in range(k):
            new_up[v] = run
            run = (run + down[v]) % MOD
        run = 0
        for v in range(k - 1, -1, -1):
            new_down[v] = run
            run = (run + up[v]) % MOD
        up, down = new_up, new_down
    return (sum(up) + sum(down)) % MOD
```
**Dry run:** k=3, n=3. Length 2: up=[0,1,2], down=[2,1,0]. new_up = exclusive prefix sums of down = [0,2,3]. new_down = exclusive suffix sums of up = [3,2,0]. Total 5+5 = **10**. ✓
**Edge cases & tests:**
- `n=1` → k. `n=2` → k(k−1) (`(2,1,3)` → 6).
- `l == r` with n ≥ 2 → 0.
- `assert zigzag_arrays(3,4,5) == 2`, `zigzag_arrays(3,1,3) == 10`.
- Brute-force cross-check over all n ≤ 5 and k ≤ 5 (50 cases). Perf: n=k=2000 runs in under 1s.

**Follow-ups:**
- *Symmetry:* mirroring v → k−1−v swaps up and down, so `down[v] = up[k−1−v]`. You only need one array, which halves the work.
- *ZigZag Arrays II (n up to 1e9):* the transition is linear, so write it as a 2k×2k (or k×k using the symmetry) matrix and use fast exponentiation, O(k³ log n). That works for small k.
- *Constraint changes to "no 3 increasing in a row" (but 3 decreasing is allowed)?* Add a run-length to the state: `up1/up2/down`, same prefix-sum trick.

**Pattern hook:** a DP whose transition sums over "all smaller / all larger previous values" signals a prefix-sum (or Fenwick tree) optimization that removes a factor of k.

## 4. LC 912 — Sort an Array (merge sort / 3-way quicksort from scratch) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** Sort an integer array ascending without any built-in sort, in O(n log n) time. n ≤ 5e4 and values are in [−5e4, 5e4].
Example: `[5,2,3,1]` → `[1,2,3,5]`. Example: `[5,1,1,2,0,0]` → `[0,0,1,1,2,5]`.

**Clarify:** Can I return a new list, or must I sort in place? (either). Are there many duplicates? (possibly, which is the reason for the 3-way partition). Is stability needed? (not for ints, but be ready to discuss it). Is there a memory limit? (it decides merge sort vs quick/heap sort).

**Approach:** Brute force: insertion or selection sort, O(n²), which times out (TLE).
**Merge sort:** split, sort halves, merge with `<=` to keep it stable. **O(n log n) always, O(n) extra.**
**Randomized quicksort, 3-way (Dutch flag):** a random pivot gives expected O(n log n). The 3-way split `<p | ==p | >p` keeps all-equal input O(n) instead of O(n²). Recursing on the smaller side and looping on the larger bounds the stack at **O(log n)**.
```python
def merge_sort(nums: List[int]) -> List[int]:      # O(n log n) always, O(n) extra, stable
    a, buf = nums[:], nums[:]
    def sort(lo: int, hi: int) -> None:            # sorts a[lo:hi]
        if hi - lo <= 1: return
        mid = (lo + hi) // 2
        sort(lo, mid); sort(mid, hi)
        i, j, k = lo, mid, lo
        while i < mid and j < hi:
            if a[i] <= a[j]: buf[k] = a[i]; i += 1  # <= keeps it stable
            else: buf[k] = a[j]; j += 1
            k += 1
        buf[k:hi] = a[i:mid] if i < mid else a[j:hi]
        a[lo:hi] = buf[lo:hi]
    sort(0, len(a))
    return a

def quick_sort(nums: List[int]) -> List[int]:      # expected O(n log n), O(log n) stack
    a = nums[:]
    def sort(lo: int, hi: int) -> None:            # sorts a[lo..hi] inclusive
        while lo < hi:
            p = a[random.randint(lo, hi)]
            lt, i, gt = lo, lo, hi                 # a[lo:lt] < p, a[lt:i] == p, a[gt+1:] > p
            while i <= gt:
                if a[i] < p: a[lt], a[i] = a[i], a[lt]; lt += 1; i += 1
                elif a[i] > p: a[i], a[gt] = a[gt], a[i]; gt -= 1
                else: i += 1
            if lt - lo < hi - gt:                  # recurse on the smaller side
                sort(lo, lt - 1); lo = gt + 1
            else:
                sort(gt + 1, hi); hi = lt - 1
    sort(0, len(a) - 1)
    return a
```
**Dry run (3-way partition):** `[5,1,1,2,0,0]` with pivot p=1. The partition ends as `[0,0 | 1,1 | 2,5]` with lt=2 and gt=3. Recurse on `[0,0]` (the smaller side), then loop on `[2,5]`.
**Edge cases & tests:** run against all three sorts (merge, quick, heap):
- `[]`, `[7]`, all-equal `[3,3,3,3]`, negatives with extremes, and reverse-sorted 1000..1.
- 50,000 equal values: the 3-way quicksort stays fast (2-way Lomuto would go O(n²) and hit Python's recursion limit).
- 300 random lists per sort compared to `sorted()` (in the test harness only).
- Stability: merge sort on (key, original index) objects keeps the original order among equal keys.

**Follow-ups:**
- *Stability:* merge sort is stable (because of `<=`). Quicksort and heap sort are not, since long-range swaps reorder equal keys. If you need stability with an unstable sort, sort by `(key, index)`.
- *Worst case:* quicksort is O(n²) with bad pivots (sorted input plus a first/last pivot, or all-equal input with a 2-way partition). The fixes are a random pivot, a 3-way partition, and introsort (switch to heap sort past a 2·log n depth, which is what C++ `std::sort` does).
- *Heap sort (O(n log n) worst case, O(1) extra, unstable):* build a max-heap bottom-up in O(n), then repeatedly swap the root to the end and sift down.
```python
def heap_sort(nums: List[int]) -> List[int]:
    a = nums[:]; n = len(a)
    def sift(i: int, size: int) -> None:
        while True:
            big, l, r = i, 2 * i + 1, 2 * i + 2
            if l < size and a[l] > a[big]: big = l
            if r < size and a[r] > a[big]: big = r
            if big == i: return
            a[i], a[big] = a[big], a[i]; i = big
    for i in range(n // 2 - 1, -1, -1): sift(i, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]; sift(0, end)
    return a
```
- *Values bounded in [−5e4, 5e4]:* counting sort runs in O(n + V). *Doesn't fit in memory:* external merge sort (sort chunks, then a k-way merge with a heap).

**Pattern hook:** "no built-in sort": merge sort when stability or a guaranteed bound matters, 3-way random quicksort for in-place speed with duplicates, heap sort for O(1) memory with a worst-case guarantee.
