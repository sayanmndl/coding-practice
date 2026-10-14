# Tier 1 — Prefix sums, hashing, Kadane

Problems (all **Tier 1**): LC 560 Subarray Sum Equals K (+974), LC 128 Longest Consecutive Sequence, LC 53 Maximum Subarray (+152, +918), LC 287 Find the Duplicate Number.
Theme: replace an O(n²) scan over (i, j) pairs with a one-pass invariant, whether that's a prefix-sum hashmap, a set with run heads, Kadane's running best, or the array read as a linked list.

## 1. LC 560 — Subarray Sum Equals K (prefix sum + hashmap) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Given an integer array `nums` (values may be negative) and an integer `k`, return the number of contiguous non-empty subarrays whose sum equals `k`.
Ex: `[1,1,1], k=2 → 2`; `[1,2,3], k=3 → 2` (`[1,2]` and `[3]`).

**Clarify:** Can values be negative or zero? (Yes, and this matters.) Do we count subarrays or check whether one exists? (Count.) Could n be large? (Up to 2·10⁴, so O(n²) is borderline and O(n) is expected.) Is the empty array allowed? (Return 0.)

**Approach:** The brute force sums every (i, j) pair: O(n²) time with running sums (O(n³) naively). **Key insight:** `sum(i..j) = P[j+1] − P[i]`, so a subarray ending at j has sum k iff some earlier prefix equals `P − k`. Keep a hashmap counting prefix values, seeded with `{0: 1}` for the empty prefix. That's **O(n) time, O(n) space.**
**Why sliding window fails:** a window needs monotonicity, where growing the window only increases the sum and shrinking only decreases it. With negatives (or zeros, when counting), extending can *decrease* the sum, so "shrink while sum > k" throws away valid starts.
```python
from collections import defaultdict
def subarray_sum(nums: list[int], k: int) -> int:   # O(n) time, O(n) space
    count = defaultdict(int); count[0] = 1          # empty prefix
    pre = ans = 0
    for x in nums:
        pre += x
        ans += count[pre - k]       # earlier prefixes that close a sum-k window
        count[pre] += 1             # add AFTER the lookup (non-empty subarrays)
    return ans
```
**Dry run** `[1,2,3], k=3`: pre=1, need −2 → 0; pre=3, need 0 → +1; pre=6, need 3 → +1. ans=2 ✓.

**Edge cases & tests:** empty input; all zeros with k=0 (n(n+1)/2); negatives that cancel; k negative.
`assert subarray_sum([1,1,1],2)==2`, `assert subarray_sum([0,0,0],0)==6`, `assert subarray_sum([1,-1,0],0)==3`, `assert subarray_sum([],0)==0`, `assert subarray_sum([3,4,7,2,-3,1,4,2],7)==4`. Plus 300 random cases against the brute force.

**Follow-ups:**
- *All values positive?* Then a sliding window works in O(1) space.
- *Return the longest subarray with sum k (LC 325)?* Store the **first** index of each prefix instead of a count, and take `max(j − first[pre−k])`.
- *2-D (LC 1074)?* Fix a pair of rows, compress the columns into a 1-D array, and run this: O(R²·C).
- *Streaming?* It already is one pass, but the map grows to O(distinct prefixes). If k is fixed and values are bounded, prefixes stay within a range you could array-index.

**Sibling: LC 974 Subarray Sums Divisible by K.** Two prefixes give a sum divisible by k iff they're **congruent mod k**, so count residues and add `count[r]` at each step. **Gotcha:** in Python `-1 % 5 == 4`, which is always non-negative for k>0. In Java/C++/Go, `-1 % 5 == -1`, so you'd need `((pre % k) + k) % k`, or else −1 and 4 land in different buckets. Say this out loud.
```python
def subarrays_div_by_k(nums: list[int], k: int) -> int:   # O(n) time, O(k) space
    count = [0] * k; count[0] = 1
    pre = ans = 0
    for x in nums:
        pre = (pre + x) % k      # Python: already in [0, k)
        ans += count[pre]
        count[pre] += 1
    return ans
# assert subarrays_div_by_k([4,5,0,-2,-3,1],5)==7; assert subarrays_div_by_k([-1,2,9],2)==2
```
**Pattern hook:** "count/longest subarrays with sum (or sum mod k) = target" with negatives allowed → prefix sum + hashmap of earlier prefixes.

## 2. LC 128 — Longest Consecutive Sequence (hash set, run heads) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Given an unsorted array of integers, return the length of the longest run of consecutive integers (in value, not position). It must run in O(n).
Ex: `[100,4,200,1,3,2] → 4` (1,2,3,4); `[0,3,7,2,5,8,4,6,0,1] → 9`.

**Clarify:** Are there duplicates? (Yes, and they count once.) Negatives? (Yes.) Empty input? (Return 0.) Is O(n) strictly required, or is sorting OK? (O(n), which rules out sorting.)

**Approach:** Sorting and scanning takes O(n log n). Brute force, where every x walks up via set lookups, is O(n²) in the worst case (`[1..n]`, starting from each element). **Key insight:** only start walking from a **run head**, meaning an x with `x−1 ∉ set`. **Amortized argument:** each element is visited by the inner `while` at most once overall, because it belongs to exactly one run and only that run's head walks over it. Total work is outer O(n) + inner Σ(run lengths) = O(n). **O(n) time, O(n) space.** Iterate over the *set* rather than the list, or with many duplicate heads you redo the same walk.
```python
def longest_consecutive(nums: list[int]) -> int:   # O(n) time, O(n) space
    s = set(nums); best = 0
    for x in s:
        if x - 1 in s:
            continue                 # not a run head; its head will cover it
        y = x
        while y + 1 in s:
            y += 1
        best = max(best, y - x + 1)
    return best
```
**Dry run** `[100,4,200,1,3,2]`: heads are 100 (len 1), 200 (len 1), and 1 (walk 2,3,4 → len 4). 4, 3 and 2 are skipped. Answer 4.

**Edge cases & tests:** empty; a single element; all duplicates; negatives crossing zero.
`assert longest_consecutive([])==0`, `assert longest_consecutive([5])==1`, `assert longest_consecutive([1,1,1])==1`, `assert longest_consecutive([-1,0,1,-3])==3`, `assert longest_consecutive([0,3,7,2,5,8,4,6,0,1])==9`.

**Follow-ups:**
- *Streaming (numbers arrive one at a time, report the best so far)?* Keep a **boundary map** `len[x]` that is valid at run endpoints. On a new x, take `l=len[x−1]` and `r=len[x+1]`, so `t=l+r+1`, then set `len[x−l]=len[x+r]=len[x]=t`. Ignore duplicates. That's O(1) per insert (tested below, 300 random streams match the batch answer).
- *Union-find?* Union x with x±1 when they're present and track component size. It's O(n α(n)) and generalizes (it also supports queries like "size of x's run"), but the set approach is simpler for the batch case.
- *Doesn't fit in memory?* Use an external sort and a single scan, or partition by value range into buckets and stitch runs that cross bucket boundaries.
```python
class StreamingLCS:                     # O(1) amortized per add
    def __init__(self) -> None:
        self.len: dict[int, int] = {}; self.best = 0
    def add(self, x: int) -> int:
        if x in self.len: return self.best
        l, r = self.len.get(x - 1, 0), self.len.get(x + 1, 0)
        t = l + r + 1
        self.len[x] = self.len[x - l] = self.len[x + r] = t
        self.best = max(self.best, t)
        return self.best
```
**Pattern hook:** "O(n), unsorted, consecutive values" → hash set + only expand from the start of each run (amortized linear).

## 3. LC 53 — Maximum Subarray (Kadane) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Given an integer array, find the contiguous non-empty subarray with the largest sum. Return the sum, and the follow-up asks for its `[l, r]` indices too.
Ex: `[-2,1,-3,4,-1,2,1,-5,4] → 6` at indices (3, 6), i.e. `[4,-1,2,1]`; `[-3,-1,-2] → -1`.

**Clarify:** Non-empty? (Yes, so all-negative input returns the max element, not 0.) Which indices on ties? (The earliest-ending best, which is fine.) Could the sum overflow? (Not in Python.)

**Approach:** Brute force over all (i, j) with running sums is O(n²). Divide and conquer is O(n log n). **Kadane recurrence:** `cur[i] = max(nums[i], cur[i−1] + nums[i])`, the best sum *ending at* i, and `ans = max cur[i]`. **Invariant:** a non-positive running prefix can never help a future subarray, so restart there. **O(n) time, O(1) space.** For indices, record `start` on each restart and snapshot `(start, i)` whenever best improves.
```python
def max_subarray(nums: list[int]) -> tuple[int, int, int]:   # O(n), O(1)
    best, bl, br = nums[0], 0, 0
    cur, start = 0, 0
    for i, x in enumerate(nums):
        if cur <= 0:
            cur, start = x, i        # negative/zero prefix only hurts: restart
        else:
            cur += x
        if cur > best:
            best, bl, br = cur, start, i
    return best, bl, br
```
**Dry run** (example): cur goes −2 → restart 1 → −2 → restart 4 (start=3) → 3 → 5 → **6** (best, (3, 6)) → 1 → 5. Returns (6, 3, 6).

**Edge cases & tests:** a single element; all negative; all positive (the whole array); zeros.
`assert max_subarray([-2,1,-3,4,-1,2,1,-5,4])==(6,3,6)`, `assert max_subarray([1])==(1,0,0)`, `assert max_subarray([-3,-1,-2])==(-1,1,1)`, `assert max_subarray([5,4,-1,7,8])==(23,0,4)`. Plus 300 random cases checked against brute force, including `sum(a[l:r+1])==best`.

**Follow-ups:**
- *Range queries "max subarray in [l, r]"?* Use a segment tree whose nodes store (total, best prefix, best suffix, best), merged in O(1). That's O(log n) per query and supports updates.
- *2-D max-sum rectangle?* Fix a pair of rows, compress the columns, and run Kadane: O(R²·C).
- *At most k elements / length ≥ L?* Use prefix sums + a sliding min of `P[j−L]`, or a monotonic deque for the bounded-length variant.

**Sibling: LC 152 Maximum Product Subarray.** A negative flips max and min, so track both the **max and min product ending here** and take the best of `(x, hi·x, lo·x)` for each. Zero resets naturally because x itself is a candidate. O(n), O(1).
```python
def max_product(nums: list[int]) -> int:
    hi = lo = best = nums[0]
    for x in nums[1:]:
        c = (x, hi * x, lo * x)
        hi, lo = max(c), min(c)
        best = max(best, hi)
    return best
# assert max_product([2,3,-2,4])==6; assert max_product([-2,3,-4])==24; assert max_product([-2,0,-1])==0
```
**Sibling: LC 918 Maximum Sum Circular Subarray.** The answer either doesn't wrap (plain Kadane) or does wrap, and a wrapping one equals `total − (min subarray)`. **Gotcha:** if everything is negative, `total − min = 0` corresponds to an empty subarray, so return `best_max` in that case. O(n), O(1).
```python
def max_circular(nums: list[int]) -> int:
    total = cmax = cmin = 0
    bmax = bmin = nums[0]
    for x in nums:
        total += x
        cmax = max(cmax + x, x); bmax = max(bmax, cmax)
        cmin = min(cmin + x, x); bmin = min(bmin, cmin)
    return bmax if bmax < 0 else max(bmax, total - bmin)
# assert max_circular([5,-3,5])==10; assert max_circular([-3,-2,-3])==-2; assert max_circular([1,-2,3,-2])==3
```
**Pattern hook:** "best contiguous subarray by sum or product" → a DP of the best value *ending at i* (Kadane), and for products also carry the min. "Circular" means total − min.

## 4. LC 287 — Find the Duplicate Number (Floyd cycle detection / binary search on value) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** `nums` has n+1 integers, each in `[1, n]`. Exactly one value is repeated, possibly many times. Return it **without modifying the array** and using **O(1) extra space**.
Ex: `[1,3,4,2,2] → 2`; `[3,1,3,4,2] → 3`.

**Clarify:** Read-only? (Yes, so no sorting and no sign-marking.) O(1) space? (Yes, so no set.) Can the duplicate appear more than twice? (Yes, which breaks the XOR/sum tricks.) Is exactly one duplicate value guaranteed? (Yes.)

**Approach:** A set is O(n) space. Sorting mutates the array. Negating `nums[|x|]` mutates it too. So:
**(a) Floyd:** treat the array as a function `i → nums[i]` on nodes 0..n. Node 0 has no incoming edge (values are ≥1), so starting from 0 the walk must eventually enter a cycle. The cycle's **entrance** has two predecessors, which means two indices map to the same value, and that value is the duplicate. Phase 1: tortoise/hare meet inside the cycle. Phase 2: **why it works.** Let μ be the distance to the entrance and λ the cycle length. At the meeting point slow has gone d steps and fast 2d, so d ≡ 0 (mod λ). Then, from the meeting point, walking μ more steps lands at μ + d ≡ μ, the entrance. So reset one pointer to the start and step both by 1, and they meet at the entrance. **O(n) time, O(1) space, read-only.**
**(b) Binary search on value:** with `cnt(m) = #{x ≤ m}`, pigeonhole says `cnt(m) > m` iff the duplicate is ≤ m, which is monotone in m. **O(n log n) time, O(1) space, read-only.** It's easier to derive under pressure.
```python
def find_duplicate(nums: list[int]) -> int:        # O(n) time, O(1) space
    slow = fast = nums[0]
    while True:                                    # phase 1: meet in cycle
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast: break
    slow = nums[0]                                 # phase 2: find entrance
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow

def find_duplicate_bs(nums: list[int]) -> int:     # O(n log n), O(1)
    lo, hi = 1, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if sum(x <= mid for x in nums) > mid: hi = mid   # dup in [lo, mid]
        else: lo = mid + 1
    return lo
```
**Dry run** `[1,3,4,2,2]`: the walk is 0→1→3→2→4→2→…, whose cycle is {2, 4} with entrance 2. Phase 1, with (slow, fast) starting at (1, 1): (3, 2) → (2, 2), so they meet at 2. Phase 2, with slow reset to nums[0]=1 and fast=2: (3, 4) → (2, 2), so they meet at **2** ✓.

**Edge cases & tests:** n=1 (`[1,1]`); every value the duplicate; the duplicate at the extreme value n; a long tail before the cycle.
Both functions pass: `[1,3,4,2,2]→2`, `[3,1,3,4,2]→3`, `[1,1]→1`, `[2,2,2,2,2]→2`, `[1,4,4,2,4]→4`, `[2,5,9,6,9,3,8,9,7,1]→9`. Plus 500 random arrays (the duplicate repeated 2..n+1 times), where both agree.

**Follow-ups:**
- *Why not sum/XOR?* They only work if the duplicate appears exactly twice and all of 1..n are present.
- *Mutation allowed?* Cyclic sort (swap x into slot x) or sign-marking gives O(n) time and O(1) space, but you must say that it mutates the input.
- *Read-only constraint in practice:* the data is shared or mmapped, or read-only memory. Binary search needs only O(log n) sequential **passes**, which is good for data on disk or streamed (no random access), whereas Floyd needs random access.
- *Multiple duplicate values?* Floyd breaks. Use a set, or a bitset of n bits (O(n) bits, still small).

**Pattern hook:** "values in [1, n], n+1 slots, read-only, O(1) space" → the array is a linked list `i → nums[i]` and Floyd finds the cycle entrance. Otherwise binary search on the value range using a count.
