# DP practice — Google style

Six problems, one per DP family. The cards in `google_coding_index.md` already cover LC 300 LIS, House Robber, Coin Change, Word Break, and 0/1 knapsack. These problems fill in the twists Google likes to add on top of those classics.

## How to drive a DP problem in the interview (say these steps out loud)
1. **State:** "Let `dp[...]` = the best/count/feasibility for ___." Name what each index means, in words, before writing code. Most DP bugs are a vague state.
2. **Transition:** what was the *last decision*? Enumerate it: take or skip, which split point `k`, which child state, which next element in a mask. Write the recurrence.
3. **Base:** the empty prefix, empty interval, null node, or empty mask. Decide whether "impossible" is `inf`, `-inf`, or 0 ways.
4. **Order:** evaluate a state only after everything it depends on: increasing prefix, increasing interval *length*, post-order for trees, increasing mask. If the order isn't obvious, use top-down `@lru_cache` and say so.
5. **Answer:** say which cell holds it (`dp[n]`, `dp[0][m-1]`, `min(root states)`, `dp[full]`). Mention reconstruction (parent pointers, or a walk back through the table) if they want the actual solution.
6. **Optimize space:** a rolling row (2D → 1D), reverse iteration for 0/1 knapsack, or keeping only the last k values. Do this *after* the correct version works, and say what you lose (usually reconstruction).

Interview cadence: brute-force recursion (exponential) → "the subproblems repeat; the state is X" → memoize → convert to bottom-up if asked → optimize space.

---

## 1. Russian Doll Envelopes, with reconstruction (LIS, 2D twist) — Hard ✅ tested
**Prompt (as asked):** Given envelopes `[w, h]`, one fits inside another only if *both* its width and height are strictly smaller. Return the longest nesting chain itself, not just its length.
Example: `[[5,4],[6,4],[6,7],[2,3]]` → `[[2,3],[5,4],[6,7]]` (length 3).

**Clarify:**
- Strict in both dimensions? → Yes; equal widths can't nest.
- Can envelopes rotate? → No.
- Do you need the chain or only its length? → The chain (any optimal one).
- n up to 1e5? → Yes, so O(n²) is too slow.

**Approach:** Brute force: sort by width, then O(n²) LIS DP with `dp[i] = 1 + max dp[j]` over j that fit inside i. Key insight: **sort by width ascending, and by height *descending* among equal widths**. Then any strictly increasing subsequence of heights can't take two envelopes with the same width, so the 2D problem reduces to a 1D strict LIS on heights. Use patience sorting: `tails[k]` = the smallest ending height of a chain of length k+1, with `bisect_left` for strictness. For reconstruction, store `tail_idx[k]` and `parent[i] = tail_idx[k-1]` at insertion time. O(n log n) time, O(n) space.
```python
from bisect import bisect_left

def max_envelopes(envs: list[list[int]]) -> list[list[int]]:
    order = sorted(envs, key=lambda e: (e[0], -e[1]))  # w asc, h desc
    tails: list[int] = []      # tails[k] = min end height of chain of len k+1
    tail_idx: list[int] = []   # index into order of that tail
    parent = [-1] * len(order)
    for i, (_, h) in enumerate(order):
        k = bisect_left(tails, h)          # strict increase -> bisect_left
        if k == len(tails):
            tails.append(h); tail_idx.append(i)
        else:
            tails[k] = h; tail_idx[k] = i
        parent[i] = tail_idx[k - 1] if k > 0 else -1
    chain, i = [], tail_idx[-1] if tail_idx else -1
    while i != -1:
        chain.append(order[i]); i = parent[i]
    return chain[::-1]
```
**Dry run:** sorted = `[2,3],[5,4],[6,7],[6,4]`. h=3 → tails=[3]. h=4 → tails=[3,4], parent=[2,3]. h=7 → tails=[3,4,7], parent=[5,4]. h=4 → bisect_left=1 replaces tails[1] (this doesn't extend the chain). Walk back from tail_idx[2] = `[6,7]` → `[5,4]` → `[2,3]`.

**Edge cases & tests:** empty input → `[]`; all identical → length 1; equal widths with different heights (the desc-height trick); a single envelope.
```python
assert len(max_envelopes([[5,4],[6,4],[6,7],[2,3]])) == 3
assert len(max_envelopes([[1,1],[1,1],[1,1]])) == 1
assert max_envelopes([]) == []
assert len(max_envelopes([[4,5],[4,6],[6,7],[2,3],[1,1]])) == 4
assert len(max_envelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])) == 3
# plus: every returned chain verified strictly nested in both dims
```
**Follow-ups:**
- *3D boxes (w, h, d)?* The sort trick only removes one dimension. You need O(n²) DP, or a sort plus a 2D BIT/CDQ divide-and-conquer for O(n log² n).
- *Non-strict (≤) nesting?* Sort h ascending among equal w, and use `bisect_right`.
- *Streaming envelopes?* `tails` maintains the length online. Reconstruction needs the parent array, which is O(n) memory.

**Pattern hook:** "chain/nest/stack items where *every* dimension must increase" → sort one dimension (descending tiebreak), then LIS on the other.

---

## 2. Edit Distance with path reconstruction (2D string DP) — Hard ✅ tested
**Prompt (as asked):** Return the minimum number of single-character inserts, deletes, and replaces needed to turn `a` into `b`, *and* one sequence of operations that achieves it.
Example: `"horse" → "ros"` = 3: `replace h->r @0`, `delete r @2`, `delete e @4`.

**Clarify:**
- Do all ops cost 1? → Yes (follow-up: weighted).
- Case-sensitive? → Yes.
- Lengths up to ~1e3–5e3? → Yes, so O(mn) is fine.
- Any optimal op list is OK? → Yes.

**Approach:** Brute force: recurse on the first mismatch with three branches, O(3^(m+n)). Insight: the state is the prefix pair. `dp[i][j]` = min ops to turn `a[:i]` into `b[:j]`. If `a[i-1]==b[j-1]` then `dp[i][j]=dp[i-1][j-1]`, else `1+min(replace dp[i-1][j-1], delete dp[i-1][j], insert dp[i][j-1])`. Base: `dp[i][0]=i`, `dp[0][j]=j`. Reconstruct by walking back from `(m,n)` and following whichever neighbour produced the value. O(mn) time and space.
```python
def edit_distance(a: str, b: str) -> tuple[int, list[str]]:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]   # dp[i][j]: a[:i] -> b[:j]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    ops, i, j = [], m, n
    while i > 0 or j > 0:
        if i and j and a[i-1] == b[j-1] and dp[i][j] == dp[i-1][j-1]:
            i, j = i - 1, j - 1
        elif i and j and dp[i][j] == dp[i-1][j-1] + 1:
            ops.append(f"replace {a[i-1]}->{b[j-1]} @{i-1}"); i, j = i - 1, j - 1
        elif i and dp[i][j] == dp[i-1][j] + 1:
            ops.append(f"delete {a[i-1]} @{i-1}"); i -= 1
        else:
            ops.append(f"insert {b[j-1]} @{i}"); j -= 1
    return dp[m][n], ops[::-1]
```
**Dry run:** `horse/ros`: dp[5][3]=3. Walk back: e≠s, so delete e (dp[4][3]=2). s=s, match. r≠o, so delete r. o=o, match. h≠r, so replace. The result is 3 ops.

**Edge cases & tests:** empty source or target (all inserts or all deletes); identical strings → 0 and `[]`; swapped pair `"ab"→"ba"` = 2.
```python
assert edit_distance("horse", "ros")[0] == 3
assert edit_distance("intention", "execution")[0] == 5
assert edit_distance("", "abc")[0] == 3 and edit_distance("abc", "")[0] == 3
assert edit_distance("same", "same") == (0, [])
assert edit_distance("kitten", "sitting")[0] == 3
# plus: applying the returned ops to a reproduces b
```
**Follow-ups:**
- *O(min(m,n)) space?* Keep two rolling rows, which loses reconstruction. To keep both, use Hirschberg's algorithm: divide and conquer on the middle row gives O(mn) time and O(n) space with the full path.
- *Is distance ≤ k?* Only fill the band `|i-j| ≤ k`, for O(k·min(m,n)). Use this for spell-check / fuzzy search.
- *Weighted ops / transpositions?* Swap in the per-op costs. Damerau adds `dp[i-2][j-2]+1` when adjacent characters are swapped.

**Pattern hook:** "transform / align / compare two sequences" → `dp[i][j]` over prefix pairs, and the last characters decide the transition.

---

## 3. Partition Equal Subset Sum → Target Sum (0/1 knapsack and its counting variant) — Medium ✅ tested
**Prompt (as asked):** (a) Can `nums` be split into two subsets with equal sums? (b) Follow-on: assign `+` or `-` to each number. How many assignments sum to `target`?
Examples: `[1,5,11,5]` → True. `[1,1,1,1,1], target=3` → 5.

**Clarify:**
- Non-negative integers? → Yes (zeros allowed in (b)).
- Sum bound? → ≤ ~2e4, so pseudo-polynomial is fine.
- In (b), does each element take exactly one sign? → Yes, so zeros double the count.
- Empty input? → (a) True, (b) 1 way when target = 0.

**Approach:** Brute force: 2^n subsets or sign vectors. Insight (a): this is subset sum to `total/2`. `dp[s]` = whether some subset sums to `s`, with `dp[s] |= dp[s-x]`, iterating `s` **descending** so each item is used at most once. Insight (b): with P = the positive set and N = the negative set, `P - N = target` and `P + N = total` give `P = (total+target)/2`. So count subsets that sum to P: `dp[s] += dp[s-x]`. Both are O(n·S) time and O(S) space.
```python
def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2: return False
    target = total // 2
    dp = [True] + [False] * target           # dp[s]: some subset sums to s
    for x in nums:
        for s in range(target, x - 1, -1):   # reverse: each item used once
            dp[s] = dp[s] or dp[s - x]
        if dp[target]: return True
    return dp[target]

def find_target_sum_ways(nums: list[int], target: int) -> int:
    total = sum(nums)                        # P = (total + target) / 2
    if abs(target) > total or (total + target) % 2: return 0
    p = (total + target) // 2
    dp = [1] + [0] * p                       # dp[s]: #subsets summing to s
    for x in nums:
        for s in range(p, x - 1, -1):
            dp[s] += dp[s - x]
    return dp[p]
```
**Dry run:** (b) `[1]*5, t=3`: total=5, P=4. After processing all five 1s, dp[4] = C(5,4) = 5.

**Edge cases & tests:** odd total; a single element; zeros (each one doubles the count); `|target| > total`; parity mismatch.
```python
assert can_partition([1,5,11,5]) and not can_partition([1,2,3,5])
assert not can_partition([1]) and can_partition([])
assert find_target_sum_ways([1,1,1,1,1], 3) == 5
assert find_target_sum_ways([0,0,1], 1) == 4
assert find_target_sum_ways([1], 2) == 0 and find_target_sum_ways([], 0) == 1
# plus: 300 random cases vs 2^n brute force
```
**Follow-ups:**
- *Why reverse iteration?* Forward iteration reuses `x` within the same pass, which turns it into unbounded knapsack (Coin Change).
- *Huge sums but small n (≤40)?* Use meet-in-the-middle: enumerate subset sums of each half, then sort and two-pointer (or Counter for counting).
- *Faster feasibility?* Use a Python int bitset: `bits |= bits << x`, then test bit `target`. That's O(n·S/64).

**Pattern hook:** "choose a subset / assign ± so a sum hits a value" → 0/1 knapsack over sums. Algebra often turns ± into subset sum.

---

## 4. Minimum Cost to Cut a Stick (interval DP) — Hard ✅ tested
**Prompt (as asked):** A stick of length `n` must be cut at the positions in `cuts`, in any order you choose. Each cut costs the current length of the piece being cut. Return the minimum total cost.
Example: `n=7, cuts=[1,3,4,5]` → 16 (order 3,5,1,4 → 7+4+3+2).

**Clarify:**
- Are cut positions distinct and strictly inside (0, n)? → Yes.
- Is n huge (1e6) while there are few cuts (≤100)? → Yes, so index the DP by cuts, not by length.
- Are cuts unsorted? → Yes; sort them.
- No cuts? → 0.

**Approach:** Brute force: try every order, O(k!). Insight: the *first* cut inside a segment splits it into two independent subproblems, and it costs the segment length no matter what comes after. Add the endpoints: `pts=[0]+sorted(cuts)+[n]`. Let `dp[i][j]` = the min cost to make all cuts strictly between `pts[i]` and `pts[j]`. Then `dp[i][j] = (pts[j]-pts[i]) + min_k(dp[i][k]+dp[k][j])`, with base `dp[i][i+1]=0`. Fill in increasing gap order. O(k³) time, O(k²) space.
```python
def min_cost_cut(n: int, cuts: list[int]) -> int:
    pts = [0] + sorted(cuts) + [n]
    m = len(pts)
    dp = [[0] * m for _ in range(m)]   # dp[i][j]: cuts strictly inside (pts[i], pts[j])
    for gap in range(2, m):            # increasing interval length
        for i in range(m - gap):
            j = i + gap
            dp[i][j] = pts[j] - pts[i] + min(dp[i][k] + dp[k][j] for k in range(i + 1, j))
    return dp[0][m - 1]
```
**Dry run:** pts=[0,1,3,4,5,7]. gap 2: dp[0][2]=3, dp[1][3]=3, dp[2][4]=2, dp[3][5]=3. Building up to dp[0][5] = 7 + min over k, with best k=2 (cut at 3): 7 + dp[0][2] + dp[2][5] = 7+3+6 = 16.

**Edge cases & tests:** no cuts → 0; a single cut → n; unsorted input; adjacent cuts.
```python
assert min_cost_cut(7, [1,3,4,5]) == 16
assert min_cost_cut(9, [5,6,1,4,2]) == 22
assert min_cost_cut(10, []) == 0
assert min_cost_cut(10, [5]) == 10
assert min_cost_cut(2, [1]) == 2
# plus: 200 random cases vs memoized brute force over remaining cuts
```
**Follow-ups:**
- *Burst Balloons?* Same skeleton: pick `k` as the **last** balloon burst in (i, j), so its neighbours are the fixed boundaries: `dp[i][j]=max(dp[i][k]+dp[k][j]+v[i]v[k]v[j])`.
- *Speed up?* The cost satisfies the quadrangle inequality, so Knuth's optimization (`opt[i][j-1] ≤ opt[i][j] ≤ opt[i+1][j]`) gives O(k²). This is the same structure as optimal BST.
- *Return the cut order?* Store the argmin `k` and emit it pre-order recursively.

**Pattern hook:** "order of operations on a segment, and cost depends on the current piece" → interval DP over boundaries. Pick the first (or last) operation as the split.

---

## 5. Binary Tree Cameras (tree DP, 3-state) — Hard ✅ tested
**Prompt (as asked):** A camera at a node monitors its parent, itself, and its children. Return the minimum number of cameras needed to monitor every node of a binary tree.
Example: `[0,0,null,0,0]` → 1 (a camera on the root's left child).

**Clarify:**
- Empty tree? → 0.
- Node count up to 1e3–1e5? → Yes; with deep trees, mention the recursion limit.
- Only the count is needed? → Yes (follow-up: placement).
- Is every node equal (no weights)? → Yes.

**Approach:** Brute force: 2^n camera subsets. Insight: post-order, where each node returns three states and every node *below* it is already covered. `has_cam` = a camera here. `covered` = no camera here, but a child has one. `not_cov` = no camera here and not covered yet, so the parent must take a camera. Transitions: `has_cam = 1 + Σ min(all child states)`. `covered = min(left has_cam + right {cam|covered}, symmetric)`. `not_cov = left covered + right covered`. A null child is (inf, 0, 0). Answer: `min(has_cam, covered)` at the root. O(n) time, O(h) stack.
```python
from typing import Optional

def min_camera_cover(root: Optional["TreeNode"]) -> int:
    INF = float("inf")
    def dfs(node):
        # returns (has_cam, covered_no_cam, not_covered); subtree below covered
        if not node: return INF, 0, 0
        la, lb, lc = dfs(node.left)
        ra, rb, rc = dfs(node.right)
        has_cam = 1 + min(la, lb, lc) + min(ra, rb, rc)
        covered = min(la + min(ra, rb), ra + min(la, lb))
        not_cov = lb + rb
        return has_cam, covered, not_cov
    a, b, _ = dfs(root)
    return min(a, b)
```
**Dry run:** In `[0,0,null,0,0]`, each leaf returns (1, inf, 0). The middle node gets has_cam = 1+0+0 = 1, covered = 2, not_cov = inf. The root gets has_cam = 1+1+0 = 2 and covered = la + min(ra,rb) = 1+0 = 1. Answer 1.

**Edge cases & tests:** an empty tree; a single node (needs 1); a path/chain; a perfect tree of 3.
```python
assert min_camera_cover(build([0,0,None,0,0])) == 1
assert min_camera_cover(build([0,0,None,0,None,0,None,None,0])) == 2
assert min_camera_cover(None) == 0
assert min_camera_cover(build([0])) == 1
assert min_camera_cover(build([0,0,0])) == 1
# plus: 300 random trees vs brute force over camera subsets
```
**Follow-ups:**
- *Greedy alternative?* Post-order with 3 status codes: a leaf's parent always gets a camera. That's also O(n), but the DP version extends to weighted node costs and the greedy doesn't.
- *General tree / graph?* The tree DP extends to n-ary trees (sum over children, and for `covered` pick the best child to "upgrade"). On a general graph this is minimum dominating set, which is NP-hard.
- *House Robber III?* It's the same skeleton with 2 states (rob, skip): `rob = v + skip_L + skip_R`, `skip = max(L) + max(R)`.

**Pattern hook:** "choose nodes in a tree with a constraint between neighbours" → post-order returning a small tuple of states per node.

---

## 6. Minimum Number of Work Sessions to Finish the Tasks (bitmask DP) — Medium ✅ tested
**Prompt (as asked):** You have `n ≤ 14` tasks with durations, and a session can hold up to `session_time` of work. A task can't be split across sessions. Return the minimum number of sessions.
Example: `tasks=[1,2,3], session_time=3` → 2 ({1,2}, {3}).

**Clarify:**
- Is each task ≤ session_time? → Yes (otherwise infeasible).
- n small (≤14–16)? → Yes; that's the signal for bitmask DP.
- Is order within a session irrelevant? → Yes.
- Empty task list? → 0.

**Approach:** Brute force: assign each task to a bin with backtracking, which is exponential and only fast with pruning. Greedy first-fit is *wrong* (this is bin packing). Insight: `dp[mask]` = the lexicographically smallest `(sessions_used, time_in_current_session)` that finishes exactly the tasks in `mask`. Fewer sessions is always better, and with equal sessions, less used time in the open session is better, so the pair is a valid DP value. Transition: add task i to the open session if it fits, otherwise open a new one. O(2ⁿ·n) time, O(2ⁿ) space.
```python
def min_sessions(tasks: list[int], session_time: int) -> int:
    n = len(tasks)
    full = 1 << n
    dp = [(n + 1, 0)] * full              # dp[mask] = (sessions, time in last)
    dp[0] = (1, 0)                        # one empty session open
    for mask in range(full):              # submasks precede supermasks
        s, t = dp[mask]
        for i in range(n):
            if mask & (1 << i): continue
            nxt = mask | (1 << i)
            cand = (s, t + tasks[i]) if t + tasks[i] <= session_time else (s + 1, tasks[i])
            if cand < dp[nxt]: dp[nxt] = cand
    return dp[full - 1][0] if n else 0
```
**Dry run:** [1,2,3], T=3. mask{1}=(1,1). Adding 2 gives {1,2}=(1,3). Adding 3 to that gives (2,3). Final dp[111] = (2,3), so the answer is 2.

**Edge cases & tests:** an empty list; a single task that fills the session; every task equal to T (n sessions); everything fits in one session.
```python
assert min_sessions([1,2,3], 3) == 2
assert min_sessions([3,1,3,1,1], 8) == 2
assert min_sessions([1,2,3,4,5], 15) == 1
assert min_sessions([4,4,4], 4) == 3
assert min_sessions([], 5) == 0 and min_sessions([5], 5) == 1
# plus: 300 random cases vs exact bin-assignment backtracking
```
**Follow-ups:**
- *Alternative?* Precompute `fits[sub]`, then use `dp[mask] = 1 + min dp[mask ^ sub]` over submasks that fit. That's O(3ⁿ), simpler to prove, and slower.
- *Shortest Path Visiting All Nodes?* BFS over states `(node, visited_mask)`. That's O(2ⁿ·n²): the same idea where the mask is the "set done so far".
- *n = 100?* Bitmask DP is infeasible, since the problem is NP-hard. Use first-fit decreasing (≤ 11/9·OPT + 1), or an ILP / branch-and-bound solver.

**Pattern hook:** "n ≤ 20 and you're assigning/ordering a *set* of items" → `dp[mask]`, iterated in increasing mask order (or as BFS over `(pos, mask)`).

---

## DP recognition table
| Problem cue | Family | State definition |
|---|---|---|
| "longest increasing / chain / nest", n up to 1e5 | LIS | `tails[k]` = min tail of an increasing subsequence of length k+1 (bisect). Use `parent[]` to rebuild the sequence |
| "every dimension must increase" (envelopes, boxes) | LIS + sort trick | sort dim1 asc and dim2 desc on ties → LIS on dim2 |
| "transform / align / common subsequence of two strings" | 2D string | `dp[i][j]` = answer for prefixes `a[:i]`, `b[:j]` |
| "pick a subset to hit sum / capacity", items used once | 0/1 knapsack | `dp[s]` = reachable / #ways / best value at sum s; iterate s descending |
| "unlimited copies of each item" | unbounded knapsack | same `dp[s]`, but iterate s ascending |
| "assign + / − to reach target" | knapsack via algebra | count subsets summing to `(total+target)/2` |
| "order of merges / cuts / bursts on a segment" | interval | `dp[i][j]` over boundaries; split at the first (cut) or last (burst) op `k`; fill by length |
| "choose tree nodes with a neighbour constraint" | tree | post-order tuple per node: (take, skip) or (cam, covered, uncovered) |
| "n ≤ 20, assign / order / visit a set" | bitmask | `dp[mask]` (+ last node / open-bin load), or BFS over `(node, mask)` |
| "count ways / probability with a few counters" | memo on counters | `dp(counts…, flag)` with `@lru_cache` |
| "can the prefix be segmented / reached" | prefix | `dp[i]` = whether `s[:i]` is achievable; transition over the last piece |
| "path on a grid / DAG, monotone moves" | grid / DAG | `dp[r][c]` from top-left neighbours, or memo DFS on the DAG |
