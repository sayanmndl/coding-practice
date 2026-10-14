# Tier 2 — Array manipulation

Four Tier 2 in-place array problems: **LC 31 Next Permutation**, **LC 189 Rotate Array**, **LC 169 Majority Element** (+229 Majority Element II), and **LC 1838 Frequency of the Most Frequent Element**.
They share one theme: find the invariant (a non-increasing suffix, a reversal identity, pair cancellation, or a cost budget) and the O(1)-space solution follows. Every solution was tested against a brute force on random inputs.

## 1. LC 31 — Next Permutation (in-place / suffix scan) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** Rearrange `nums` in place into the next lexicographically greater permutation. If none exists (the array is fully descending), wrap around to the smallest permutation (sorted ascending). Use O(1) extra space.
Examples: `[1,2,3] → [1,3,2]`, `[3,2,1] → [1,2,3]`, `[1,1,5] → [1,5,1]`.

**Clarify:** Can there be duplicates? *Yes, so use `>=`/`<=` comparisons.* Should it wrap to sorted when at the max? *Yes.* Must it be in place? *Yes, O(1) space.* Can it be empty or length 1? *Handle both as no-ops.*

**Approach:** Brute force: generate all permutations, sort them, and take the next one. That's O(n!·n).
**Key insight:** The longest non-increasing suffix is already at its *maximum* arrangement, so no rearrangement of the suffix alone can make the array bigger. The change must happen at the pivot `i = ` the index just before that suffix (the rightmost `nums[i] < nums[i+1]`).
1. Swap `nums[i]` with the **smallest suffix element that is > nums[i]**. Because the suffix is non-increasing, that is the *rightmost* such element. This makes the smallest possible increase at position `i`.
2. After the swap, the suffix is *still* non-increasing (the swapped-in value fits the order), so reversing it gives the suffix's *minimum* arrangement.
Why this is the *next* permutation: the prefix before `i` is unchanged (any change further left would be a bigger jump), position `i` increases by the least possible amount, and the suffix is minimal. If there's no pivot, the whole array is descending, and reversing it gives the sorted wrap-around. **O(n) time, O(1) space.**
```python
def next_permutation(nums: List[int]) -> None:   # O(n) time, O(1) space
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:   # find rightmost ascent
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:              # rightmost element > pivot
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    lo, hi = i + 1, n - 1                      # suffix is non-increasing: reverse it
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1; hi -= 1
```
**Dry run:** `[1,5,8,4,7,6,5,3,1]`. The suffix `7,6,5,3,1` is non-increasing, so the pivot is `i=3` (value 4). The rightmost value >4 is 5 at `j=6`. Swapping gives `[1,5,8,5,7,6,4,3,1]`. Reversing the suffix gives `[1,5,8,5,1,3,4,6,7]`.

**Edge cases & tests:**
- Fully descending → sorted (`i = -1`, so the reversal covers the whole array).
- Duplicates `[1,1,5]`; all equal `[2,2,2]` → unchanged. Length 0/1 → no-op.
- `assert t([1,2,3])==[1,3,2]`; `assert t([3,2,1])==[1,2,3]`; `assert t([1,1,5])==[1,5,1]`; `assert t([1,3,2])==[2,1,3]`; `assert t([2,2,2])==[2,2,2]`
- I also ran 300 random arrays with duplicates against `sorted(set(permutations))`.

**Follow-ups:**
- *Previous permutation?* Mirror it: find the rightmost `nums[i] > nums[i+1]`, swap with the rightmost element `< nums[i]`, then reverse the suffix.
- *k-th permutation (LC 60)?* Use the factorial number system: pick digit `k // (n-1)!` from the remaining digits. That's O(n²), with no need to iterate.
- *Next greater number with the same digits (LC 556)?* Run the same algorithm on the digit list, then check for 32-bit overflow and return -1 if there's no next.

**Pattern hook:** "next/previous in lexicographic order, in place" → scan from the right for the first break in monotonicity, make the minimal swap, then reverse the suffix.

## 2. LC 189 — Rotate Array (reversal / cyclic replacement) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** Rotate `nums` right by `k` steps, in place.
Examples: `[1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]`, `[-1,-100,3,99], k=2 → [3,99,-1,-100]`.

**Clarify:** Can `k` be larger than `n`? *Yes, so take `k %= n`.* Rotate right or left? *Right.* Must it be in place with O(1) extra space? *Yes.* Can it be empty? *Treat as a no-op.*

**Approach:** Brute force: shift by 1, k times. That's O(n·k). A copy into an extra array is O(n) time but O(n) space.
**Reversal trick:** Write the array as `A B`, with `|B| = k`. The goal is `B A`. Use the identity `rev(rev(A B)) = A B` and `rev(A B) = rev(B) rev(A)`. So reverse the whole array to get `rev(B) rev(A)`, then reverse each part to get `B A`. **O(n) time, O(1) space**, about 2n swaps.
**Cyclic replacements:** Move each element directly to `(i+k) % n`, carrying the displaced one forward. A cycle returns to its start after `n/g` steps, where `g = gcd(n,k)`, so there are `g` cycles, starting at `0..g-1`. Stop when `moved == n`. O(n) time, O(1) space, exactly n writes.
```python
def rotate(nums: List[int], k: int) -> None:          # O(n) time, O(1) space
    n = len(nums)
    if n == 0: return
    k %= n
    def rev(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1; hi -= 1
    rev(0, n - 1); rev(0, k - 1); rev(k, n - 1)

def rotate_cyclic(nums: List[int], k: int) -> None:   # O(n) time, O(1) space
    n = len(nums)
    if n == 0: return
    k %= n
    moved, start = 0, 0
    while moved < n:                       # gcd(n,k) cycles of length n/gcd
        cur, carry = start, nums[start]
        while True:
            nxt = (cur + k) % n
            nums[nxt], carry = carry, nums[nxt]
            cur = nxt; moved += 1
            if cur == start: break
        start += 1
```
**Dry run:** For the reversal on `[1..7], k=3`, the steps are: full reverse `[7,6,5,4,3,2,1]` → reverse first 3 `[5,6,7,4,3,2,1]` → reverse the rest `[5,6,7,1,2,3,4]`. For the cyclic version on `n=6, k=4`, `gcd=2`, so the cycles are `0→4→2→0` and `1→5→3→1`.

**Edge cases & tests:**
- `k=0` or `k%n==0` → unchanged. `n=1`. `n=0` (guard against `% 0`). With `gcd>1`, a naive single cycle stops early.
- `assert t([1,2,3,4,5,6,7],3)==[5,6,7,1,2,3,4]`; `assert t([1],5)==[1]`; `assert t([],3)==[]`; `assert t([1,2,3,4,5,6],4)==[3,4,5,6,1,2]`; `assert t([1,2,3],3)==[1,2,3]`
- I tested both versions on 300 random `(n,k)` pairs against slicing.

**Follow-ups:**
- *Rotate left?* Use `k' = n - k%n`, or reverse the parts first and then the whole array.
- *Rotate a string or a linked list (LC 61)?* For a list: find the length, connect it into a ring, then break it at `n - k%n`.
- *Fewest writes (e.g. flash memory)?* The cyclic version writes each slot exactly once. The reversal does about 2n writes but is more cache-friendly, so it's usually faster in practice.

**Pattern hook:** "rearrange blocks in place" → it's a composition of reversals (rotate array, reverse words in a string, swap two adjacent blocks).

## 3. LC 169 — Majority Element (Boyer–Moore voting) — Easy — Tier 2 ✅ tested
**Prompt (as asked):** Return the element that appears more than `⌊n/2⌋` times. The problem guarantees it exists. Follow-up: O(n) time, O(1) space.
Examples: `[3,2,3] → 3`, `[2,2,1,1,1,2,2] → 2`.

**Clarify:** Is a majority guaranteed? *Yes. If not, add a verification pass.* Can there be negatives? *Yes, which doesn't matter.* Is it streaming? *It can be, since this is one pass.*

**Approach:** Hash count: O(n) time / O(n) space. Sorting and taking `nums[n//2]`: O(n log n). Random pick plus a check: expected O(n).
**Boyer–Moore:** Keep a `cand` and a `count`. A matching element gives +1 and any other gives −1. When `count` hits 0, adopt the next element as the candidate.
**Proof sketch:** Each decrement pairs one copy of `cand` with one *different* element, and both are "cancelled". Removing a pair of two distinct values keeps the majority a majority in what's left (it loses at most 1 of the 2 removed). When `count` hits 0, the prefix so far is fully paired off, so the majority still holds strictly more than half of the remaining suffix. By induction, the final candidate is the one survivor. Pairs number at most n/2, and the majority has more than n/2 copies, so it can't be fully cancelled. **O(n) time, O(1) space.**
```python
def majority_element(nums: List[int]) -> int:   # O(n) time, O(1) space
    cand, count = None, 0
    for x in nums:
        if count == 0:
            cand = x
        count += 1 if x == cand else -1
    return cand
```
**Dry run:** For `[2,2,1,1,1,2,2]`, `(cand,count)` goes: (2,1) (2,2) (2,1) (2,0) → (1,1) at the fifth element → (1,0) → (2,1) at the last. The result is 2.

**Edge cases & tests:**
- `n=1`. The majority shows up only at the end. Negative values.
- `assert majority_element([3,2,3])==3`; `assert majority_element([2,2,1,1,1,2,2])==2`; `assert majority_element([7])==7`; `assert majority_element([1,1,2])==1`; `assert majority_element([-1,-1,-1,5,5])==-1`
- I also ran 300 random shuffled arrays with a planted majority.

**Follow-ups:**
- *Majority not guaranteed?* Do a second pass to count `cand`, and return it only if `count > n//2`.
- *Streaming or distributed?* The state is `(cand, count)`. To merge two shards, keep the candidate with the larger count. If they're the same, add the counts; otherwise subtract the smaller count. Then verify in a second pass. For heavy hitters at more than n/k frequency, use **Misra–Gries** with k−1 counters.
- **LC 3737 — Count Subarrays With Majority Element I** (newer Google-list entry): count the subarrays where `target` is a strict majority. **Prefix balance:** map `target → +1` and everything else `→ −1`, and let `P` be the prefix sums with `P[0]=0`. Subarray `(i, j]` qualifies when `P[j] > P[i]`, so for each `j` count the earlier prefixes that are strictly smaller. The balance moves by ±1 per step, so maintain `less` incrementally from a frequency array: O(n). (A BIT or merge-sort count is O(n log n), and the n≤1000 brute force is O(n²).) Tested against brute force:
```python
def count_majority_subarrays(nums: List[int], target: int) -> int:  # O(n)
    n = len(nums); freq = [0] * (2 * n + 2); freq[n] = 1
    bal = less = ans = 0                  # less = #earlier prefixes < bal
    for x in nums:
        if x == target: less += freq[bal + n]; bal += 1
        else: bal -= 1; less -= freq[bal + n]
        ans += less; freq[bal + n] += 1
    return ans
```

**Sibling: LC 229 — Majority Element II (> ⌊n/3⌋)** — Medium ✅ tested
At most **2** elements can appear more than n/3 times. Generalize Boyer–Moore to 2 candidates with 2 counters. If `x` matches a candidate, increment it. Otherwise, fill an empty slot. Otherwise, decrement **both** (this cancels a triple of distinct values). The candidates are only *possible* answers, so a **verification pass is mandatory**. O(n) time, O(1) space.
```python
def majority_element_ii(nums: List[int]) -> List[int]:  # O(n) time, O(1) space
    c1, c2, n1, n2 = None, None, 0, 0
    for x in nums:
        if x == c1: n1 += 1
        elif x == c2: n2 += 1
        elif n1 == 0: c1, n1 = x, 1
        elif n2 == 0: c2, n2 = x, 1
        else: n1 -= 1; n2 -= 1
    return [c for c in (c1, c2) if c is not None and nums.count(c) > len(nums) // 3]
```
Tests: `[3,2,3]→[3]`, `[1,2]→[1,2]`, `[1,2,3]→[]`, `[]→[]`, `[1,1,1,3,3,2,2,2]→[1,2]`, plus 500 random arrays checked against a Counter. The match checks must come *before* the empty-slot checks. Otherwise you could set `c2` equal to `c1`.

**Pattern hook:** "element above n/k frequency, O(1) space" → k−1 cancelling candidates (Boyer–Moore / Misra–Gries), then verify.

## 4. LC 1838 — Frequency of the Most Frequent Element (sort + sliding window) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** In one operation you may increment any element by 1. With at most `k` operations in total, return the maximum possible frequency of any element.
Examples: `[1,2,4], k=5 → 3` (everything becomes 4), `[1,4,8,13], k=5 → 2`, `[3,9,6], k=2 → 1`.

**Clarify:** Are only increments allowed? *Yes, so the target must be ≥ every element raised to it.* Is the target always an existing value? *The optimum is always an existing value, since raising past it only costs more.* What are the ranges? *n ≤ 1e5, values ≤ 1e5, k ≤ 1e5. Python ints don't overflow, but in other languages use int64 for `x*len`.*

**Approach:** Brute force: for each target, greedily raise the closest smaller values. That's O(n²) after sorting.
**Key insight:** After sorting, the best set to raise to `nums[hi]` is a *contiguous* window ending at `hi`, because the nearest smaller values are the cheapest to raise. **Budget invariant:** the cost of window `[lo, hi]` is `nums[hi]·len − sum(window)`, which must be ≤ k. Moving `hi` right only increases the cost (the target grows), and moving `lo` right only decreases it, so the window is monotone and two pointers work. **O(n log n) for the sort, then an O(n) window, with O(1) extra space** (or O(n) if you can't mutate the input).
```python
def max_frequency(nums: List[int], k: int) -> int:   # O(n log n) time, O(1) extra
    nums.sort()
    lo, total, best = 0, 0, 0              # total = sum(nums[lo..hi])
    for hi, x in enumerate(nums):
        total += x
        while x * (hi - lo + 1) - total > k:   # cost to raise window to x
            total -= nums[lo]; lo += 1
        best = max(best, hi - lo + 1)
    return best
```
**Dry run:** For `[1,4,8,13], k=5`: at hi=1 (4), the cost is 4·2−5=3 ≤ 5, so best=2. At hi=2 (8), the cost is 8·3−13=11 > 5, so drop 1 and the cost becomes 8·2−12=4, giving best=2. At hi=3 (13), the cost is 13·3−25=14, so drop 4, which gives 26−21=5 ≤ 5, and best=2.

**Edge cases & tests:**
- `k=0` → the answer is the largest count of an existing value. With a single element the answer is 1. All equal → n. A large gap that exactly fits the budget.
- `assert max_frequency([1,2,4],5)==3`; `assert max_frequency([1,4,8,13],5)==2`; `assert max_frequency([3,9,6],2)==1`; `assert max_frequency([5],0)==1`; `assert max_frequency([2,2,2],0)==3`; `assert max_frequency([1,100000],99999)==2`
- I also ran 500 random cases against the greedy brute force.

**Follow-ups:**
- *Non-shrinking window variant?* Replace the `while` with an `if`, so the window never shrinks and its final size is the answer. It's the same O(n) with fewer branches.
- *Both increments and decrements allowed (LC 2968 / 2448-style)?* The cheapest target becomes the window's **median**. Compute the cost from prefix sums: `med·(m−lo) − sum_left + sum_right − med·(hi−m)`. Then use the same sliding window, or binary search on length.
- *Streaming inserts?* Keep a sorted container plus prefix sums (Fenwick tree over values). For each query, binary search the leftmost `lo` per `hi` in O(log² n).

**Pattern hook:** "max subset size where cost-to-equalize ≤ budget" → sort, then a two-pointer window with a running sum, with cost = `max·len − sum`.
