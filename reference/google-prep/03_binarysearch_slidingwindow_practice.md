# Binary search & sliding window practice — Google style

Seven problems for the two thinnest areas on the revision cards. Every solution was run against hand-written asserts and randomized brute-force checks before it was pasted here.

**Binary search template (first-true / lower bound).** Name a monotone predicate `ok(x)` that is False...False, True...True. Then:
```python
lo, hi = smallest_possible, largest_possible   # answer guaranteed in [lo, hi]
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid        # mid might be the answer; keep it
    else:       lo = mid + 1    # mid is definitely not the answer
return lo
```
Invariant: the answer is always in `[lo, hi]`. Because `hi = mid` with a floor mid, the range always shrinks, so it can't loop forever. "Binary search on the answer" means `ok` is a greedy feasibility check.

**Sliding window, "shrink while invalid".** Expand `right` every step. `while window invalid: move left`. After the loop the window is the longest valid window ending at `right`. This works only when validity is monotone: if a window is valid, every sub-window is valid too.

**"At most K" trick.** "Exactly K" isn't monotone, but "at most K" is. Count `atMost(K) - atMost(K-1)`, where `atMost` adds `right - left + 1` per step (the number of valid windows ending at `right`).

## 1. Capacity to Ship Packages within D Days / Koko Eating Bananas (binary search on the answer) — Medium ✅ tested
**Prompt (as asked):** Packages with `weights` must ship in order, across at most `days` days. Each day the ship loads consecutive packages up to its capacity. Return the minimum capacity.
Example: `weights=[1..10], days=5 → 15` (`[1-5][6,7][8][9][10]`). `[3,2,2,4,1,4], 3 → 6`.

**Clarify:** Order fixed? *Yes, contiguous.* Weights positive integers? *Yes.* `days >= 1`? *Yes.* Is an empty day allowed? *Yes, so "≤ days" is fine.*

**Approach:** Brute force: try every capacity from `max(w)` to `sum(w)`, each with an O(n) check, for O(n·S) total. Insight: `days_needed(cap)` is non-increasing in `cap`, so `ok(cap) = days_needed(cap) <= days` is monotone. Binary search it over `[max(w), sum(w)]`. The lower bound is `max(w)` because any smaller capacity can't carry the heaviest package. Total O(n log S), O(1) space.
```python
def ship_within_days(weights: List[int], days: int) -> int:
    def days_needed(cap: int) -> int:
        need, load = 1, 0
        for w in weights:
            if load + w > cap:
                need += 1
                load = 0
            load += w
        return need

    lo, hi = max(weights), sum(weights)   # answer is in [lo, hi]
    while lo < hi:                        # find first cap with days_needed <= days
        mid = (lo + hi) // 2
        if days_needed(mid) <= days:
            hi = mid                      # mid works; answer <= mid
        else:
            lo = mid + 1                  # mid fails; answer > mid
    return lo

def min_eating_speed(piles: List[int], h: int) -> int:   # Koko: same template
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if sum((p + mid - 1) // mid for p in piles) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
```
**Dry run:** `[3,2,2,4,1,4], 3`: lo=4, hi=16. mid=10: 2 days, ok, so hi=10. mid=7: 3 days, ok, so hi=7. mid=5: `[3,2][2][4,1][4]` is 4 days, fail, so lo=6. mid=6: `[3,2][2,4][1,4]` is 3 days, ok, so hi=6. Return 6.

**Edge cases & tests:** single package; capacity equals max; one day means sum; all equal.
- `assert ship_within_days([1,2,3,4,5,6,7,8,9,10], 5) == 15`
- `assert ship_within_days([7], 1) == 7`
- `assert ship_within_days([5,5,5], 1) == 15 and ship_within_days([5,5,5], 3) == 5`
- `assert min_eating_speed([3,6,7,11], 8) == 4`
- `assert min_eating_speed([10**9], 2) == 5*10**8`

**Follow-ups:**
- *Real-valued answer (e.g. min speed as a float)?* Loop a fixed number of iterations (about 60) with `hi = mid` / `lo = mid` and return `hi` within epsilon.
- *Huge n, streamed weights?* Each check is one streaming pass, so it needs O(log S) passes and O(1) memory. With multiple machines, compute `days_needed` per shard plus boundary carry. Since the check is sequential, simplest is to pass the carry-in load along the shards.
- *Minimize days given capacity?* That's just `days_needed(cap)`, the greedy check alone.

**Pattern hook:** "minimize the maximum / find the smallest X such that feasible", where feasibility is greedy and monotone, means binary search on the answer.

## 2. Search in Rotated Sorted Array II — with duplicates (binary search, LC 81) — Medium ✅ tested
**Prompt (as asked):** A non-decreasing array, possibly with duplicates, was rotated at an unknown pivot. Return whether `target` is present.
Example: `[2,5,6,0,0,1,2], 0 → True`; `target 3 → False`; `[1,0,1,1,1], 0 → True`.

**Clarify:** Duplicates allowed? *Yes, which is the twist over LC 33 (already on a card).* Return a bool or an index? *Bool.* Empty input? *Return False.* Is the worst case acceptable? *Discuss it.*

**Approach:** Brute force: linear scan, O(n). Insight from LC 33: one of `[lo..mid]` or `[mid..hi]` is always sorted, so check whether target falls in the sorted half's range. Duplicates break the "which half is sorted" test when `nums[lo] == nums[mid] == nums[hi]` (e.g. `[1,0,1,1,1]`). In that case you can't tell, but `nums[lo]` and `nums[hi]` aren't the target (they equal `nums[mid]`), so shrink both ends. Average O(log n), worst case O(n) (all equal except one). That worst case is unavoidable, so say it out loud.
```python
def search(nums: List[int], target: int) -> bool:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True
        if nums[lo] == nums[mid] == nums[hi]:   # can't tell which half is sorted
            lo += 1
            hi -= 1
        elif nums[lo] <= nums[mid]:             # left half [lo..mid] is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                   # right half [mid..hi] is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False
```
**Dry run:** `[1,0,1,1,1], 0`: lo=0, hi=4, mid=2 (1). All three ends are 1, so lo=1, hi=3. mid=2 (1). `nums[1]=0 <= 1`, so the left half [0,1] is sorted, and `0 <= 0 < 1`, so hi=1. mid=1 (0). Found it.

**Edge cases & tests:** empty; single element hit/miss; two elements rotated; target only in the "hidden" spike.
- `assert search([], 5) is False`
- `assert search([1], 1) and not search([1], 0)`
- `assert search([3,1], 1)`
- `assert search([1,3,1,1,1], 3)`
- `assert search([1]*9 + [13] + [1]*12, 13)`
Also randomized against `target in a` (3000 cases).

**Follow-ups:**
- *Why does `nums[lo] <= nums[mid]` mean the left half is sorted?* Once the all-equal case is excluded, `nums[lo] <= nums[mid]` rules out the drop being inside `(lo, mid]`. Without duplicates this is exactly LC 33.
- *Find the minimum / rotation point with duplicates (LC 154)?* Compare `nums[mid]` with `nums[hi]`: if greater, `lo = mid+1`; if less, `hi = mid`; if equal, `hi -= 1`. Worst case O(n) again.
- *Return the first index of target?* Find the pivot (LC 154 logic, careful with equal runs), then lower-bound search in the correct half.

**Pattern hook:** for a rotated array, find the sorted half and test the range. With duplicates, add an "equal ends, shrink both" escape hatch and state the O(n) worst case.

## 3. Median of Two Sorted Arrays (partition binary search, LC 4) — Hard ✅ tested
**Prompt (as asked):** Given sorted arrays `a` (size m) and `b` (size n), return the median of their union in O(log(min(m, n))).
Example: `[1,3], [2] → 2.0`; `[1,2], [3,4] → 2.5`.

**Clarify:** Can one be empty? *Yes, but not both.* Duplicates? *Yes.* Return a float? *Yes.* Integer overflow? *Not an issue in Python.*

**Approach:** Brute force: merge, O(m+n). Or two pointers to the middle, O(m+n) time and O(1) space. Insight: the median splits the union into a left part of size `half = (m+n+1)//2` and a right part. Taking `i` elements from `a` forces `j = half - i` from `b`. The partition is valid iff `a[i-1] <= b[j]` and `b[j-1] <= a[i]`, using ±inf at the borders. If `a[i-1] > b[j]` then `i` is too big, else too small. That's monotone in `i`, so binary search `i ∈ [0, m]` over the shorter array. Odd total: median = max(left side). Even total: average of max(left) and min(right). O(log min(m,n)), O(1).
```python
def find_median_sorted_arrays(a: List[int], b: List[int]) -> float:
    if len(a) > len(b):
        a, b = b, a                       # binary search the shorter array
    m, n = len(a), len(b)
    half = (m + n + 1) // 2               # size of the left partition
    lo, hi = 0, m                         # i = # elements taken from a
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < m else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < n else float("inf")
        if a_left <= b_right and b_left <= a_right:     # valid partition
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1                    # took too many from a
        else:
            lo = i + 1                    # took too few from a
    raise ValueError("inputs must be sorted and not both empty")
```
**Dry run:** `a=[1,2], b=[3,4]`: half=2, lo=0, hi=2. i=1, j=1: a_left=1, a_right=2, b_left=3, b_right=4. `b_left=3 > a_right=2`, so too few from a, lo=2. i=2, j=0: a_left=2, a_right=inf, b_left=-inf, b_right=3. Valid. Even total: (max(2,-inf) + min(inf,3)) / 2 = 2.5.

**Edge cases & tests:** one empty array; all of `a` less than all of `b`; duplicates; odd/even totals.
- `assert find_median_sorted_arrays([1,3], [2]) == 2.0`
- `assert find_median_sorted_arrays([], [1]) == 1.0`
- `assert find_median_sorted_arrays([1,1,1], [1,1]) == 1.0`
- `assert find_median_sorted_arrays([1,2,3,4], [10,11,12]) == 4.0`
- `assert find_median_sorted_arrays([5,6], [1,2,3,4]) == 3.5`
Also randomized against `statistics.median` (3000 cases).

**Follow-ups:**
- *Why search the shorter array?* It guarantees `0 <= j <= n` for every `i ∈ [0, m]`, and gives log(min) time.
- *Kth smallest of two sorted arrays?* Same partition with `half = k`, or the classic "drop k/2 from the side with the smaller k/2-th element" recursion. O(log k).
- *Median across many sorted shards that don't fit on one machine?* Binary search on the value: for a candidate `v`, sum `bisect_right(shard, v)` across shards (each in O(log)) and find the smallest `v` with count ≥ k. That takes O(log(range) · S · log n) and also works for streams via counting.

**Pattern hook:** "median / kth of two sorted arrays in log time" means binary searching a partition point with a cross-comparison validity check.

## 4. Split Array Largest Sum (binary search on the answer + greedy check, LC 410) — Hard ✅ tested
**Prompt (as asked):** Split `nums` (non-negative) into `k` non-empty contiguous subarrays, minimizing the largest subarray sum. Return that minimum.
Example: `[7,2,5,10,8], k=2 → 18` (`[7,2,5] [10,8]`). `[1,2,3,4,5], 2 → 9`.

**Clarify:** Non-negative values? *Yes, which is what makes greedy work.* `1 <= k <= len(nums)`? *Yes.* Exactly k pieces? *Yes, but "≤ k pieces achieve limit L" implies exactly k can too: just split further, since that never increases the max.* Return the value only? *Yes.*

**Approach:** Brute force DP: `dp[p][i] = min over j of max(dp[p-1][j], sum(j..i))`, O(k·n²). Insight: it's the same shape as problem 1 (shipping in k days). `pieces_needed(L)` (greedily pack each piece up to L) is non-increasing in L, so binary search the smallest L in `[max, sum]` with `pieces_needed(L) <= k`. Greedy is optimal for a fixed L because extending the current piece never hurts later pieces. O(n log S), O(1).
```python
def split_array(nums: List[int], k: int) -> int:
    def pieces_needed(limit: int) -> int:
        pieces, cur = 1, 0
        for x in nums:
            if cur + x > limit:           # start a new piece (greedy: pack as much as possible)
                pieces += 1
                cur = 0
            cur += x
        return pieces

    lo, hi = max(nums), sum(nums)
    while lo < hi:                        # first limit with pieces_needed <= k
        mid = (lo + hi) // 2
        if pieces_needed(mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo
```
**Dry run:** `[7,2,5,10,8], 2`: lo=10, hi=32. mid=21: `[7,2,5][10,8]` is 2 pieces, ok, so hi=21. mid=15: `[7,2,5][10][8]` is 3, fail, so lo=16. mid=18: 2, ok, so hi=18. mid=17: `[7,2,5][10][8]` is 3, fail, so lo=18. Return 18.

**Edge cases & tests:** k = n (answer = max); k = 1 (answer = sum); zeros; single element.
- `assert split_array([7,2,5,10,8], 2) == 18`
- `assert split_array([1,4,4], 3) == 4`
- `assert split_array([10], 1) == 10`
- `assert split_array([0,0,0], 2) == 0`
- `assert split_array([2,3,1,2,4,3], 6) == 4`
Also randomized against the O(k·n²) DP (1500 cases).

**Follow-ups:**
- *Negative numbers allowed?* The greedy and monotonicity break. Fall back to the DP, O(k·n²); it can be sped up but that's rarely expected.
- *Return the actual split?* After finding L, run the greedy once more and record the cut points. If it uses fewer than k pieces, split the largest remaining pieces arbitrarily (sums only decrease).
- *Same problem in disguise:* allocate books to k students, painter's partition, ship in D days (#1). Same code. *Maximize the minimum* (e.g. Magnetic Force Between Balls) is the mirror image: find the last true with `mid = (lo+hi+1)//2`.

**Pattern hook:** "split into k contiguous groups, minimize the max (or maximize the min)" means binary search on the answer plus a greedy count.

## 5. Longest Substring with At Most K Distinct → Subarrays with Exactly K Distinct (at-most-K trick, LC 340 → LC 992) — Medium → Hard ✅ tested
**Prompt (as asked):** (a) Return the length of the longest substring of `s` with at most `k` distinct characters. (b) Follow-on: count subarrays of `nums` with **exactly** `k` distinct integers.
Example: (a) `"eceba", 2 → 3` ("ece"). (b) `[1,2,1,2,3], 2 → 7`.

**Clarify:** k = 0? *Answer 0.* Unicode or ints? *Hashable; use a dict.* Is the count small enough? *Up to n(n+1)/2, fine in Python.* Empty input? *0.*

**Approach:** Brute force: all O(n²) windows with a running set. (a) "At most K distinct" is monotone (shrinking a window can't add distinct values), so use shrink-while-invalid: grow `right`, and while `len(count) > k` move `left`. O(n). (b) "Exactly K" is not monotone: shrinking can drop below K. Use `exactly(K) = atMost(K) - atMost(K-1)`. In `atMost`, each `right` contributes `right - left + 1` windows (every start in `[left, right]` is valid). O(n) time, O(k) space.
```python
def longest_at_most_k_distinct(s: str, k: int) -> int:
    count: dict = defaultdict(int)
    left = best = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        while len(count) > k:             # shrink while invalid
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best

def count_at_most_k(nums: Sequence, k: int) -> int:
    count: dict = defaultdict(int)
    left = total = 0
    for right, x in enumerate(nums):
        count[x] += 1
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        total += right - left + 1         # every subarray ending at right, starting in [left, right]
    return total

def subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    return count_at_most_k(nums, k) - count_at_most_k(nums, k - 1)
```
**Dry run (b):** `[1,2,1,2,3]`. atMost(2): window adds per right are 1, 2, 3, 4, then at right=4 (3) the window shrinks to `[2,3]` for 2. Total 12. atMost(1): adds 1, 1, 1, 1, 1, total 5. 12 − 5 = 7.

**Edge cases & tests:** k = 0; k larger than the distinct count (b gives 0); all equal; empty.
- `assert longest_at_most_k_distinct("eceba", 2) == 3`
- `assert longest_at_most_k_distinct("abc", 0) == 0 and longest_at_most_k_distinct("", 2) == 0`
- `assert subarrays_with_k_distinct([1,2,1,2,3], 2) == 7`
- `assert subarrays_with_k_distinct([1,1,1], 1) == 6`
- `assert subarrays_with_k_distinct([1,2], 3) == 0`
Also randomized against brute force (2000 cases each).

**Follow-ups:**
- *Streaming characters, answer (a) online?* The same loop works, but shrinking needs `s[left]`, so keep the current window's characters in a deque (O(window) memory). To cut that to O(k), store the window as a deque of runs `(char, run_length)`; it still lets you evict from the left.
- *Single pass for (b)?* Keep two left pointers (`left_far` for ≤K, `left_near` for ≤K−1) and add `left_near - left_far` per step. Same O(n), one pass.
- *Same trick elsewhere:* Count Nice Subarrays (exactly k odds), Binary Subarrays with Sum (exactly S, non-negative).

**Pattern hook:** "count subarrays with EXACTLY k <something monotone>" means atMost(k) − atMost(k−1).

## 6. Sliding Window Maximum (monotonic deque, LC 239) — Hard ✅ tested
**Prompt (as asked):** Given `nums` and window size `k`, return the max of every contiguous window of size k.
Example: `[1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]`.

**Clarify:** `1 <= k <= n`? *Assume yes; return [] for empty input.* Negatives or duplicates? *Yes.* Output length? *n − k + 1.* Streaming? *Possible follow-up.*

**Approach:** Brute force: max of each window, O(n·k). Better: a heap of `(-val, idx)` with lazy deletion of out-of-window tops, O(n log n). Optimal: a monotonic deque of **indices** whose values are strictly decreasing front to back. A new value `x` pops every back element `<= x`, since those are older and no larger, so they can never be a future max. The front is the current max; pop it once its index `<= i - k`. Each index is pushed and popped at most once, so O(n) amortized time and O(k) space.
```python
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    dq: deque = deque()                   # indices; nums[dq] strictly decreasing
    out: List[int] = []
    for i, x in enumerate(nums):
        if dq and dq[0] <= i - k:         # front fell out of the window
            dq.popleft()
        while dq and nums[dq[-1]] <= x:   # x dominates smaller, older values
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```
**Dry run:** `[1,3,-1,-3,5,3,6,7], 3` (dq shown as values). i0: [1]. i1: 3 pops 1, [3]. i2: [3,-1], emit 3. i3: [3,-1,-3], emit 3. i4: index 1 (the 3) is expired, popleft; 5 pops -1 and -3, [5], emit 5. i5: [5,3], emit 5. i6: 6 pops 3 and 5, [6], emit 6. i7: [7], emit 7.

**Edge cases & tests:** k = 1 (identity); k = n (single max); decreasing input (deque grows to k); duplicates (`<=` pop keeps the newest copy).
- `assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]`
- `assert max_sliding_window([1,-1], 1) == [1,-1]`
- `assert max_sliding_window([1,2,3,4], 4) == [4]`
- `assert max_sliding_window([9,8,7,6], 2) == [9,8,7]`
- `assert max_sliding_window([4,4,4], 2) == [4,4]`
Also randomized against brute force (2000 cases).

**Follow-ups:**
- *Streaming / time-based window ("max latency in the last 60 s")?* Store `(timestamp, value)` in the deque and expire from the front by `ts <= now - 60`. Memory is bounded by the decreasing run, not by k.
- *Window min, or max − min ≤ limit (LC 1438)?* Two deques (max and min) plus a shrink-while-invalid variable window.
- *Sliding window median?* A deque doesn't work, because the median isn't decomposable this way. Use two heaps with lazy deletion (already on a card, LC 480).

**Pattern hook:** "max/min over a moving window", or "next greater within range", means a monotonic deque of indices.

## 7. Substring with Concatenation of All Words (variable window with counts, LC 30) — Hard ✅ tested
*(Swapped in for Minimum Window Substring, LC 76, which is already a card. 76 vs 727 is covered precisely in the follow-ups.)*

**Prompt (as asked):** Given `s` and a list of equal-length `words` (which may repeat), return every start index where `s` contains a concatenation of all of `words`, each used exactly once, in any order.
Example: `s="barfoothefoobarman", words=["foo","bar"] → [0, 9]`. `s="barfoofoobarthefoobarman", ["bar","foo","the"] → [6, 9, 12]`.

**Clarify:** All words the same length? *Yes (w).* Duplicate words? *Yes, so multiplicities matter.* Overlapping answers? *Yes, return all.* Empty `words`? *Return [].*

**Approach:** Brute force: for each of n starts, chop the next `m` words and compare Counters, O(n·m·w). Insight: a valid window is word-aligned, so split `s` into `w` lanes (offsets `0..w-1`). In each lane, slide a window **one word at a time** with a `have` Counter:
- If the word isn't in `need`, no window can cross it, so reset and jump `left` past it.
- Otherwise add it. **Shrink while invalid:** while `have[word] > need[word]`, evict from the left.
- If `matched == m`, the window is an exact permutation of the words. Record `left`, then evict one word to continue.
Each word enters and leaves each lane once, so O(n·w) total time (word slicing costs w), O(m·w) space.
```python
def find_substring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []
    w, n_words = len(words[0]), len(words)
    need = Counter(words)
    res: List[int] = []
    for offset in range(w):               # w independent word-aligned "lanes"
        left, matched = offset, 0
        have: Counter = Counter()
        for right in range(offset, len(s) - w + 1, w):
            word = s[right:right + w]
            if word not in need:          # hard reset: no window can span this word
                have.clear()
                matched, left = 0, right + w
                continue
            have[word] += 1
            matched += 1
            while have[word] > need[word]:    # shrink while invalid (too many of word)
                have[s[left:left + w]] -= 1
                matched -= 1
                left += w
            if matched == n_words:        # window is exactly a permutation of words
                res.append(left)
                have[s[left:left + w]] -= 1   # slide by one word to keep searching
                matched -= 1
                left += w
    return sorted(res)
```
**Dry run:** `"barfoothefoobarman", ["foo","bar"]`, offset 0: "bar", then "foo", so matched=2: record 0 and evict "bar" (left=3). "the" isn't a word: reset, left=9. "foo", then "bar": matched=2, record 9. "man": reset. Offsets 1 and 2 never match a word. Result `[0, 9]`.

**Edge cases & tests:** duplicate words; overlapping matches; `s` shorter than the concatenation; a word appearing too often (shrink path).
- `assert find_substring("barfoothefoobarman", ["foo","bar"]) == [0,9]`
- `assert find_substring("wordgoodgoodgoodbestword", ["word","good","best","good"]) == [8]`
- `assert find_substring("aaaaaa", ["aa","aa"]) == [0,1,2]`
- `assert find_substring("a", ["a","a"]) == []`
- `assert find_substring("", ["a"]) == []`
Also randomized against the brute force (2000 cases).

**Follow-ups:**
- **Minimum Window Substring (LC 76) vs Minimum Window Subsequence (LC 727). Be precise:**
  - *76:* t's characters **with multiplicity, any order, gaps allowed** must appear in a contiguous window of s. Use a Counter of t, `required = len(need)` (distinct chars), and `formed` = number of chars with `have[c] == need[c]`. Increment `formed` only when `have[c]` *reaches* `need[c]`, and decrement it only when it *drops below*. Expand `right`. **While `formed == required`**, record the window, then evict `s[left]`. This is "shrink while **valid**" (minimizing), the mirror of shrink-while-invalid. O(|s| + |t|). `"ADOBECODEBANC", "ABC" → "BANC"`.
  - *727:* t must appear **in order** as a subsequence, so counts can't express it and a sliding window doesn't apply. Scan forward until all of t is matched at end `e`, then scan **backward** from `e` matching t in reverse to find the tightest start. Record it, restart from start+1. O(|s|·|t|) worst case. `"abcdebdde", "bde" → "bcde"` (both "bcde" and "bdde" have length 4; the **leftmost** wins). Your prev card's dry run ends at "bdde" while it states "bde": re-check it against this tie-break rule, and remember the answer is a contiguous window of s, so it includes any gap characters.
- *Words of different lengths?* Lanes break. Use a trie plus DFS/backtracking from each start, or DP over positions. Much harder; say so.
- *Very long s, streamed?* Run the `w` lanes in parallel with one `have` Counter each, fed by a rolling buffer of the last `m·w` characters.

**Pattern hook:** "a window that must contain exactly/at least these counts" means a Counter plus `formed`/`matched`. Shrink while invalid for exact matches; shrink while valid to minimize.
