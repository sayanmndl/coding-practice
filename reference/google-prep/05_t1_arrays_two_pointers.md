# Tier 1 — Arrays & two pointers

Covers four Tier 1 must-do array problems: **LC 42 Trapping Rain Water** (two pointers + monotonic stack), **LC 15 3Sum** (sort + two pointers, sibling LC 16 3Sum Closest), **LC 238 Product of Array Except Self** (prefix/suffix), and **LC 41 First Missing Positive** (cyclic sort / index hashing).
All solutions were run against hand-written asserts plus randomized brute-force cross-checks.

## 1. LC 42 — Trapping Rain Water (two pointers / monotonic stack) — Hard — Tier 1 ✅ tested
**Prompt (as asked):** Given non-negative bar heights of width 1, compute how much rain water is trapped.
Example: `[0,1,0,2,1,0,1,3,2,1,2,1]` → `6`; `[4,2,0,3,2,5]` → `9`.

**Clarify:** Are heights non-negative ints? (yes) Empty input? (return 0) Can n be ~1e5? (yes, so O(n) is needed) Can I mutate the input? (not needed)

**Approach:** water[i] = min(maxLeft[i], maxRight[i]) − h[i]. Brute force recomputes both maxes per i, O(n²). Prefix/suffix max arrays give O(n) time and O(n) space. **Two pointers** get it to O(1) space.
**Correctness argument:** `lmax = max(h[0..l])` is exactly maxLeft[l]. We only need maxLeft[l] ≤ maxRight[l] when we settle l, because then water[l] = lmax − h[l] regardless of what the unseen middle holds. Proof: we advance l only when `h[l] < h[r]`. Every left bar we ever passed (including the current one) was strictly shorter than some right-pointer bar at that moment, and all of those right bars lie at or right of the current r. So lmax < some bar in h[r..n-1] ≤ maxRight[l]. Hence min(maxLeft, maxRight) = lmax and the water at l is final. The right side is symmetric (ties go right, which is safe by the same argument with ≤).
**Monotonic stack:** keep a stack of indices with decreasing heights. When `h[i]` is taller than the top, pop the `bottom`; the new top is the left wall, so add a horizontal layer of `(min(h[left], h[i]) − h[bottom]) × (i − left − 1)`. This fills water by layers rather than by columns.

```python
def trap(h: list[int]) -> int:                 # O(n) time, O(1) space
    l, r = 0, len(h) - 1
    lmax = rmax = water = 0
    while l < r:
        if h[l] < h[r]:
            lmax = max(lmax, h[l]); water += lmax - h[l]; l += 1
        else:
            rmax = max(rmax, h[r]); water += rmax - h[r]; r -= 1
    return water

def trap_stack(h: list[int]) -> int:           # O(n) time, O(n) space
    st: list[int] = []                         # indices, heights decreasing
    water = 0
    for i, x in enumerate(h):
        while st and h[st[-1]] < x:
            bottom = st.pop()
            if not st: break                   # no left wall
            left = st[-1]
            water += (min(h[left], x) - h[bottom]) * (i - left - 1)
        st.append(i)
    return water
```
**Dry run (two pointers, `[4,2,0,3,2,5]`):** h[l]=4 < h[r]=5 → lmax=4, +0; l=1: lmax=4, +2; l=2: +4; l=3: +1; l=4: +2; l=5 = r, stop. Total 9.

**Edge cases & tests:** empty, a single bar, strictly increasing (0), a flat plateau, a `[3,0,3]` basin, and a 2000-case random cross-check against the brute force.
`assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6`; `assert trap([4,2,0,3,2,5]) == 9`; `assert trap([]) == 0`; `assert trap([1,2,3,4]) == 0`; `assert trap([3,0,3]) == 3`.

**Follow-ups:**
- *Streaming heights?* The two-pointer method needs both ends. The stack version is online: it emits water as soon as a right wall arrives, and its memory is O(depth of the decreasing run).
- *2D elevation map (LC 407)?* Use a min-heap BFS from the border: always expand the lowest boundary cell, and water = max(0, boundary − h).
- *Which is better in an interview?* Lead with prefix/suffix arrays (easy to explain), then compress to two pointers. Give the stack version if asked for an alternative or a streaming answer.

**Pattern hook:** "water/area bounded by min of two sides" → min(leftMax, rightMax); move the pointer on the smaller side.

## 2. LC 15 — 3Sum (sort + two pointers) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Return all *unique* triplets `[a,b,c]` from `nums` with a+b+c = 0.
Example: `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`; `[0,0,0,0]` → `[[0,0,0]]`.

**Clarify:** Uniqueness is by value, not by index? (yes) Does output order matter? (no) n ≤ 3000? (yes, so O(n²) is fine) Can I sort or copy the input? (yes)

**Approach:** Brute force over all triples with a set is O(n³). Hash-based 2Sum per i is O(n²) time but dedupe is messy. **Sort + two pointers:** fix i, then run 2Sum on `nums[i+1:]` with l/r pointers, which is O(n²) time and O(1) extra space (excluding the sort and output).
**Dedupe logic:** (1) skip `i` when `nums[i] == nums[i-1]`, so the same anchor value is never reused; (2) after a hit, advance `l` past equal values (r then moves past its duplicates naturally, since the sum would be > 0 with the same l value); (3) early exit when `nums[i] > 0`, because everything to the right is also positive.

```python
def three_sum(nums: list[int]) -> list[list[int]]:   # O(n^2) time, O(1) extra
    nums = sorted(nums); n = len(nums); res = []
    for i in range(n - 2):
        if nums[i] > 0: break
        if i and nums[i] == nums[i - 1]: continue     # dedupe anchor
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0: l += 1
            elif s > 0: r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l - 1]: l += 1   # dedupe l
    return res
```
**Dry run:** sorted `[-4,-1,-1,0,1,2]`. i=0 (−4): no pair sums to 4. i=1 (−1): l=−1, r=2 → 0, hit `[-1,-1,2]`; l→0, r→1 → 0, hit `[-1,0,1]`. i=2 has a duplicate −1, so skip. i=3 (0): l=1, r=2 → 3 > 0, then r moves and the loop ends.

**Edge cases & tests:** all zeros, no solution, empty/short input, duplicates on both sides, and a 2000-case random cross-check against `itertools.combinations`.
`assert three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]`; `assert three_sum([0,0,0,0]) == [[0,0,0]]`; `assert three_sum([0,1,1]) == []`; `assert three_sum([]) == []`; `assert three_sum([-2,0,0,2,2]) == [[-2,0,2]]`.

**Follow-ups:**
- *Can't sort / need indices?* Per i, run a hash-set 2Sum and dedupe with a set of sorted tuples. That is O(n²) time and O(n) space.
- *4Sum / kSum (LC 18)?* Recurse: fix k−2 anchors with the same skip-duplicates rule, then two pointers at the base. O(n^(k−1)).
- *Count triplets with sum < target (LC 259)?* When `s < target`, add `r − l` and move l; otherwise move r.

**Pattern hook:** "unique k-tuples summing to X" → sort, fix anchors, two pointers, and skip equal neighbours.

**Sibling: LC 16 — 3Sum Closest.** Return the sum of three numbers closest to `target`. Use the same sort + anchor + two pointers, but track `best` by `|s − target|`. Move l when `s < target` and r when `s > target`. Return immediately on an exact match. O(n²) time, O(1) extra space. No dedupe is needed because we return a value, not a set.
```python
def three_sum_closest(nums: list[int], target: int) -> int:
    nums = sorted(nums); best = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(best - target): best = s
            if s < target: l += 1
            elif s > target: r -= 1
            else: return s
    return best
# assert three_sum_closest([-1,2,1,-4], 1) == 2; ([0,0,0],1) == 0; ([1,1,1,0],100) == 3
```

## 3. LC 238 — Product of Array Except Self (prefix/suffix products) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Return `out` where `out[i]` = the product of all `nums[j]` with j ≠ i. **No division**, O(n) time, and O(1) extra space (the output array doesn't count).
Example: `[1,2,3,4]` → `[24,12,8,6]`; `[-1,1,0,-3,3]` → `[0,0,9,0,0]`.

**Clarify:** Can there be zeros and negatives? (yes) Does the product fit in an int? (guaranteed 32-bit; Python ints are unbounded anyway) Is n ≥ 2? (yes) Does the output count as extra space? (no)

**Approach:** Brute force multiplies everything except i for each i, O(n²). Total product ÷ nums[i] is banned and breaks on zero. **Key insight:** out[i] = prefix[i] × suffix[i]. Write the prefix products into `out` on a left-to-right pass, then sweep right-to-left with a single running `suffix` scalar. O(n) time, O(1) extra space.
Invariant: on the backward pass, before processing i, `suffix = ∏ nums[i+1..n-1]` and `out[i] = ∏ nums[0..i-1]`.

```python
def product_except_self(nums: list[int]) -> list[int]:   # O(n) time, O(1) extra
    n = len(nums); out = [1] * n
    for i in range(1, n):
        out[i] = out[i - 1] * nums[i - 1]     # prefix product of nums[:i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix                      # times product of nums[i+1:]
        suffix *= nums[i]
    return out
```
**Dry run (`[1,2,3,4]`):** the prefix pass gives `[1,1,2,6]`. The suffix pass: i=3 → 6×1=6, suffix=4; i=2 → 2×4=8, suffix=12; i=1 → 1×12=12, suffix=24; i=0 → 1×24=24. Result `[24,12,8,6]`.

**Edge cases & tests:** one zero, two zeros, n=2, negatives, and a 1000-case random cross-check against `math.prod`.
`assert product_except_self([1,2,3,4]) == [24,12,8,6]`; `assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]`; `assert product_except_self([0,0,2]) == [0,0,0]`; `assert product_except_self([5,7]) == [7,5]`; `assert product_except_self([2,-3,4]) == [-12,8,-6]`.

**Follow-ups:**
- *Zeros (if division were allowed)?* Count zeros and take the product of the non-zeros, P. With **0 zeros**, out[i] = P / nums[i]. With **1 zero** at index z, out[z] = P and every other entry is 0. With **≥2 zeros**, the whole output is 0. The prefix/suffix solution handles all three cases with no special casing, which is why it is preferred.
- *Overflow in a fixed-width language?* Work in log space (sum of logs, tracking the sign and zero count separately), or use modular products if the answer is wanted mod p. Division is not available mod p unless the values are coprime to p, which is another reason for prefix/suffix.
- *Streaming / data too big for memory?* Make two passes over the stream. Pass 1 writes the prefix products to disk. Pass 2 reads in reverse and multiplies in the running suffix. Alternatively, a segment tree supports point updates plus "product excluding i" in O(log n).

**Pattern hook:** "f(everything except i)" with an associative op and no inverse → prefix[i] ⊕ suffix[i].

## 4. LC 41 — First Missing Positive (cyclic sort / in-place index hashing) — Hard — Tier 1 ✅ tested
**Prompt (as asked):** Given an unsorted int array, return the smallest missing positive integer in O(n) time and O(1) extra space.
Example: `[3,4,-1,1]` → `2`; `[7,8,9,11,12]` → `1`; `[1,2,0]` → `3`.

**Clarify:** Can there be negatives, zeros, and duplicates? (yes) May I mutate the input? (yes, which is the whole trick) Empty input? (return 1) Are values up to 2³¹? (yes, so no counting array sized by value)

**Approach:** Sort and scan is O(n log n). A hash set is O(n) time but O(n) space. **Key insight:** the answer lies in `[1, n+1]`, because n slots can hold at most 1..n. So use the array itself as the hash table: put value v at index v−1 (cyclic sort). Then the first index i with `nums[i] != i+1` gives the answer i+1, and if every slot is filled the answer is n+1.
Each swap places one value permanently at its home, so there are at most n swaps total: **O(n) time, O(1) space**. The guard `nums[v-1] != v` (not `i != v-1`) prevents infinite loops on duplicates.

```python
def first_missing_positive(nums: list[int]) -> int:   # O(n) time, O(1) extra
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1                       # home of nums[i]
            nums[i], nums[j] = nums[j], nums[i]   # j computed first: safe swap
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```
**Dry run (`[3,4,-1,1]`):** i=0: 3 → swap with idx 2 → `[-1,4,3,1]`; −1 is out of range, stop. i=1: 4 → idx 3 → `[-1,1,3,4]`; 1 → idx 0 → `[1,-1,3,4]`; −1, stop. i=2 and i=3 are already home. Scan: idx 1 holds −1 ≠ 2, so return **2**.

**Edge cases & tests:** empty, all out of range, duplicates (`[1,1]`), already a permutation (returns n+1), single `[1]`, and a 2000-case random check against a naive scan.
`assert first_missing_positive([1,2,0]) == 3`; `assert first_missing_positive([3,4,-1,1]) == 2`; `assert first_missing_positive([7,8,9,11,12]) == 1`; `assert first_missing_positive([]) == 1`; `assert first_missing_positive([1,1]) == 2`; `assert first_missing_positive([2,1]) == 3`.

**Follow-ups:**
- *Alternative without swaps?* The sign-marking trick: replace non-positives and values > n with n+1, then for each |v| ≤ n make `nums[|v|-1]` negative. The first positive index i gives i+1.
- *Can't mutate the input?* Then O(1) space is impossible in general. Use a bitset of size n+1 (n/8 bytes), or binary search on the answer with counting passes for O(n log n) time and O(1) space.
- *Streaming / huge data?* The answer is ≤ (count of items)+1. Keep a bitmap over [1, N+1], or shard by range and find the first range whose count of distinct in-range values is less than its width (an external-memory version of the same pigeonhole).

**Pattern hook:** "values in [1..n], O(1) space, find missing/duplicate" → cyclic sort: value v belongs at index v−1.
