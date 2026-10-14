# Tier 2 — Greedy & stack contribution

All four problems are **Tier 2**: LC 2007 Find Original Array From Doubled Array (sort + counter greedy), LC 907 Sum of Subarray Minimums (monotonic-stack contribution, with LC 2104 as a follow-up), LC 32 Longest Valid Parentheses (stack of indices, plus an O(1)-space two-pass version), and LC 1526 Minimum Number of Increments on Subarrays (greedy difference, with proof).
Every solution was run against hand-written asserts and randomized brute-force cross-checks before being pasted here.

## 1. LC 2007 — Find Original Array From Doubled Array (sort + counter greedy) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** `changed` was made by taking `original`, appending `2*x` for every `x`, and shuffling. Return `original`, or `[]` if `changed` isn't a doubled array.
Examples: `[1,3,4,2,6,8] → [1,3,4]`, and `[6,3,0,1] → []`.

**Clarify:**
- Can there be negatives? *LC says 0 ≤ x, but handle them anyway (Google twist).*
- Zeros? *Yes. 0 pairs with itself, so the count of zeros must be even.*
- Any order for the output? *Yes.*
- Size? *Up to 1e5, so O(n log n) is fine.*

**Approach:** Brute force: try every pairing / repeatedly search for a partner, which is O(n²). **Key insight:** the smallest element (by absolute value) can't be anyone's double, so it *must* be an original, and its partner is forced to be `2x`. Greedy: walk the distinct values in increasing `|x|` and match all `cnt[x]` copies against `2x`. For negatives, `-2`'s double is `-4`, which is larger in absolute value, so sorting by `abs` gives one uniform rule. Zero is its own double, so it needs `cnt[0]` to be even. **O(n + k log k)** time (k = distinct values), O(n) space.
```python
def findOriginalArray(changed: List[int]) -> List[int]:   # O(n + k log k) time, O(n) space
    if len(changed) % 2: return []
    cnt = Counter(changed)
    res: List[int] = []
    for x in sorted(cnt, key=abs):          # abs order handles negatives
        if cnt[x] == 0: continue
        if x == 0:
            if cnt[0] % 2: return []
            res += [0] * (cnt[0] // 2); continue
        if cnt[2 * x] < cnt[x]: return []
        cnt[2 * x] -= cnt[x]
        res += [x] * cnt[x]
    return res
```
**Dry run:** `[1,3,4,2,6,8]`. x=1 consumes one 2, giving res=[1]. x=2 now has cnt 0, so skip. x=3 consumes 6, giving [1,3]. x=4 consumes 8, giving [1,3,4]. x=6 and x=8 are at 0, so skip.

**Edge cases & tests:**
- Odd length → `[]` immediately. Empty → `[]`.
- Zeros: `[0,0,0,0] → [0,0]` and `[0,0,0] → []` (the explicit zero branch avoids "0 consumes itself" bugs).
- Negatives: `[-2,-4,1,2] → [-2,1]` (a plain ascending sort would visit -4 first and fail).
- Duplicates: `[2,1,2,4,2,4] → [1,2,2]`.
```python
assert sorted(findOriginalArray([1,3,4,2,6,8])) == [1,3,4]
assert findOriginalArray([6,3,0,1]) == []
assert findOriginalArray([0,0,0]) == [] and findOriginalArray([0,0,0,0]) == [0,0]
assert sorted(findOriginalArray([-2,-4,1,2])) == [-2,1]
```
**Follow-ups:**
- *Values bounded (≤1e5)?* Use a counting array indexed by value instead of sort, for O(n + V).
- *Factor k instead of 2 (LC 954 is "array of doubled pairs")?* Same greedy with `k*x`. LC 954 already allows negatives, which is exactly where the abs-sort matters.
- *Streaming?* You can't decide until the end, but you can keep the counter online and run the greedy at query time over the distinct keys.

**Pattern hook:** "pair each x with f(x), where f is monotone": the extreme element has a forced partner, so sort and greedily match with a counter.

## 2. LC 907 — Sum of Subarray Minimums (monotonic stack contribution) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** Given `arr`, return the sum of `min(sub)` over every contiguous subarray, mod 1e9+7.
Example: `[3,1,2,4] → 17` (the minimums are 3,1,1,1,1,1,1,2,2,4).

**Clarify:**
- Duplicates? *Yes, which is the whole tie-breaking issue.*
- Values positive? *1..3e4, n ≤ 3e4, so O(n²) is borderline and O(n) is expected.*
- Mod only at the end? *Python ints are unbounded, so apply it at the end. In other languages, take it per term.*

**Approach:** Brute force: for each start, extend while tracking the running min. That's O(n²). **Contribution insight:** flip the sum. Instead of asking for the min of each subarray, count how many subarrays have `arr[i]` as their min. If `L` = distance to the previous smaller element and `R` = distance to the next smaller element, then `arr[i]` is the min of `L*R` subarrays, so the answer is `Σ arr[i]*L*R`. **Tie-breaking:** with equal values, a subarray like `[2,2]` would be counted for *both* 2s if both sides used strict `<`. Make one side strict and the other non-strict: left stops at a **strictly smaller** element (pop `>=`), and right stops at a **smaller-or-equal** element (pop `>`). Then each subarray's min is credited to exactly one index, the **rightmost** occurrence of the min: element i's range extends left over equal values but stops at an equal value on the right. Either convention works as long as it's asymmetric. **O(n)** time and space.
```python
def sumSubarrayMins(arr: List[int]) -> int:   # O(n) time, O(n) space
    MOD = 10**9 + 7
    n = len(arr)
    left = [0] * n   # dist to previous STRICTLY smaller
    right = [0] * n  # dist to next smaller-OR-EQUAL
    st: List[int] = []
    for i in range(n):
        while st and arr[st[-1]] >= arr[i]: st.pop()
        left[i] = i - (st[-1] if st else -1); st.append(i)
    st = []
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] > arr[i]: st.pop()
        right[i] = (st[-1] if st else n) - i; st.append(i)
    return sum(a * l * r for a, l, r in zip(arr, left, right)) % MOD
```
One-pass variant (also tested): append a `-inf` sentinel. When `m` is popped at index `i`, `i` is its right boundary and the new stack top is its left boundary, so add `A[m]*(m-l)*(i-m)`.

**Dry run:** `[3,1,2,4]` gives left=[1,2,1,1] and right=[1,3,2,1]. Then 3·1·1 + 1·2·3 + 2·1·2 + 4·1·1 = 3+6+4+4 = **17**.

**Edge cases & tests:**
- Single element. All equal `[2,2,2] → 12` (catches double counting: using the same comparison on both sides gives 18 or 6).
- Strictly increasing or decreasing, `[1,2,3] → 10`, `[3,2,1] → 10`.
```python
assert sumSubarrayMins([3,1,2,4]) == 17
assert sumSubarrayMins([11,81,94,43,3]) == 444
assert sumSubarrayMins([2,2,2]) == 12 and sumSubarrayMins([5]) == 5
assert sumSubarrayMins([1,2,3]) == sumSubarrayMins([3,2,1]) == 10
```
**Follow-ups:**
- **LC 2104 Sum of Subarray Ranges:** Σ(max − min) = Σmax − Σmin. Σmax is the same routine on negated values. O(n), versus the O(n²) brute force that is also accepted. (Tested code below.)
- *Sum of subarray maxima?* Flip the comparisons, or negate the input.
- *Streaming appends?* Keep the stack plus a running `dp[i]` = sum of mins of subarrays ending at i: `dp[i] = dp[j] + arr[i]*(i-j)`, where j = previous smaller. That's amortized O(1) per append.
```python
def subArrayRanges(nums: List[int]) -> int:   # LC 2104, O(n)
    def total(sign: int) -> int:              # sum of mins of sign*nums
        A, st, res = [sign * x for x in nums] + [float('-inf')], [], 0
        for i, x in enumerate(A):
            while st and A[st[-1]] >= x:
                m = st.pop(); l = st[-1] if st else -1
                res += A[m] * (m - l) * (i - m)
            st.append(i)
        return res
    return int(-total(-1) - total(1))         # sum(max) - sum(min)
```
**Pattern hook:** "sum over all subarrays of min/max": flip it to per-element contribution with previous/next-smaller boundaries, made strict on one side and non-strict on the other.

## 3. LC 32 — Longest Valid Parentheses (stack of indices / two-pass counter) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** Given a string of only `(` and `)`, return the length of the longest well-formed (valid) parentheses **substring**.
Examples: `"(()" → 2`, and `")()())" → 4`.

**Clarify:**
- Substring (contiguous), not subsequence? *Substring. A subsequence would just be 2·matched pairs.*
- Only those two characters? *Yes.*
- Empty string? *Return 0.*
- Is O(1) space wanted? *Ask. That's the usual follow-up.*

**Approach:** Brute force: check every substring for validity, O(n³), or O(n²) by extending each start with a balance counter. Also possible: DP where `dp[i]` = longest valid substring ending at i, O(n). **Stack-of-indices insight:** keep a stack whose **bottom is the index just before the current valid run** (seeded with `-1`, and replaced on each unmatched `)`). Push the index of each `(`. On `)`, pop. If the stack is now empty, this `)` is unmatched and becomes the new base. Otherwise the current valid run is `i - st[-1]`. O(n) time and space.
**O(1)-space two-pass:** scan left→right counting `open`/`close`. When they're equal, record `2*close`. When `close > open`, reset both. This misses runs where `(` stays in excess, as in `"(()"`, so also scan right→left with the roles swapped (reset when `open > close`). Any maximal valid substring is caught by at least one pass. O(n) time, O(1) space.
```python
def longestValidParentheses(s: str) -> int:   # O(n) time, O(n) space
    st: List[int] = [-1]          # bottom = index before current valid run
    best = 0
    for i, c in enumerate(s):
        if c == '(':
            st.append(i)
        else:
            st.pop()
            if not st: st.append(i)       # unmatched ')' -> new base
            else: best = max(best, i - st[-1])
    return best

def lvp_O1(s: str) -> int:                    # O(n) time, O(1) extra space
    best = 0
    for seq, op in ((s, '('), (s[::-1], ')')):  # in-place: iterate reversed indices
        o = c = 0
        for ch in seq:
            if ch == op: o += 1
            else: c += 1
            if o == c: best = max(best, 2 * c)
            elif c > o: o = c = 0
    return best
```
(`s[::-1]` copies the string. To be truly O(1), loop `for i in range(n-1, -1, -1)`.)

**Dry run (stack):** `")()())"`, starting with st=[-1]. i0 `)` pops, the stack is empty, so st=[0]. i1 `(` gives [0,1]. i2 `)` pops, giving len 2-0=2. i3 `(` gives [0,3]. i4 `)` pops, giving 4-0=**4**. i5 `)` pops, the stack is empty, so st=[5]. Answer 4.

**Edge cases & tests:** empty string; all `(`; `"))(("`; nested plus adjacent `"()(())" → 6`; a broken prefix `"()(()" → 2` (the left pass alone would get this wrong).
```python
for f in (longestValidParentheses, lvp_O1):
    assert f("(()") == 2 and f(")()())") == 4 and f("") == 0
    assert f("()(())") == 6 and f("()(()") == 2
    assert f("((((") == 0 and f("))((") == 0
```
(Also cross-checked against the brute force on 3000 random strings.)

**Follow-ups:**
- *Return the substring itself?* Track `start = st[-1] + 1` whenever `best` improves.
- *Multiple bracket types `()[]{}`?* The counter trick breaks (balance alone doesn't prove validity). Use the stack of indices and also check that the popped char matches. If it doesn't, treat the position as a new base and clear the stack to it.
- *Minimum removals to make it valid (LC 1249)?* Same stack, and the leftover indices are the ones to delete.

**Pattern hook:** "longest valid bracket substring": a stack of *indices* with a sentinel base. If O(1) space is demanded, a balance counter both directions.

## 4. LC 1526 — Minimum Number of Increments on Subarrays to Form a Target Array (greedy difference) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** Start from an all-zero array the same length as `target`. One operation adds 1 to every element of any contiguous subarray. Return the minimum number of operations to reach `target`.
Examples: `[1,2,3,2,1] → 3`, and `[3,1,5,4,2] → 7`.

**Clarify:**
- Values ≥ 1? *Yes (1..1e5), n ≤ 1e5.*
- Only increments, no decrements? *Yes.*
- Just the count, not the operations? *Count. (The operations can be reconstructed, see the follow-ups.)*

**Approach:** Brute force: repeatedly subtract 1 from every maximal positive segment and count the segments. That's O(n·max). Divide and conquer (take the min, split on it) is O(n²) worst case. **Insight:** look at differences. With `prev` = previous value (0 before index 0), answer = `Σ max(0, target[i] − target[i−1])`. O(n) time, O(1) space.
**Proof.** *Lower bound:* define `d_i = t[i] − t[i−1]` (with `t[−1] = 0`). An operation on `[l, r]` raises `t[l]` relative to `t[l−1]` by 1, i.e. it increases exactly one difference, `d_l`, by +1 (it may decrease `d_{r+1}`, which never helps a positive difference). So each operation raises at most one positive difference by 1, and every `d_i > 0` needs at least `d_i` operations *starting* at i. That gives ops ≥ Σ max(0, d_i). *Achievability:* sweep left to right while holding a set of "open" operations equal in number to the current height. When the height rises by `d > 0`, open `d` new ops at i. When it falls, close the excess ops at i−1. Each op is a contiguous interval and the heights match exactly, so Σ positive rises operations suffice. Equivalently, think of the array as a skyline: each rise starts new horizontal "layers", and a drop just ends layers that already exist.
```python
def minNumberOperations(target: List[int]) -> int:   # O(n) time, O(1) space
    ops, prev = 0, 0
    for x in target:
        ops += max(0, x - prev)    # only rises need new operations
        prev = x
    return ops
```
**Dry run:** `[3,1,5,4,2]` has rises +3, (−2), +4, (−1), (−2), so 3 + 4 = **7**.

**Edge cases & tests:**
- A single element `[5] → 5`. Flat `[1,1,1,1] → 1`.
- Valley/zigzag `[1,5,1,5] → 9` (the second peak needs new ops, because the first ones had to close at the valley).
- Monotone decreasing: the answer is `t[0]`.
```python
assert minNumberOperations([1,2,3,2,1]) == 3
assert minNumberOperations([3,1,1,2]) == 4
assert minNumberOperations([3,1,5,4,2]) == 7
assert minNumberOperations([5]) == 5 and minNumberOperations([1,1,1,1]) == 1
assert minNumberOperations([1,5,1,5]) == 9
```
(Also cross-checked against the layer-peeling brute force on 2000 random arrays.)

**Follow-ups:**
- *Streaming?* It's already one pass with O(1) state (`prev`, `ops`).
- *Start from an arbitrary `initial` array?* Work on `diff = target − initial`. With only increments, it's infeasible if any diff < 0, and otherwise it's the same formula on `diff`. If both +1 and −1 ops are allowed (LC 3229), run the formula separately over the positive and negative runs (reset `prev` to 0 when the sign flips).
- *Circular array, or 2D?* 2D doesn't decompose cleanly. Discuss it as an open problem, or treat each row independently if ops are row-segments.
- *Output the operations?* Use the achievability sweep: a stack of open start indices, push `d` starts on a rise and pop on a fall, emitting `[start, i−1]`.

**Pattern hook:** "add 1 to a subarray, minimum ops to reach target": take differences and sum the positive rises (the skyline/layer argument). Same idea as LC 122 stock profit (Σ positive deltas).
