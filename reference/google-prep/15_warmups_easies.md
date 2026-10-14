# Warm-ups — high-frequency easies (30–45 min batch)

Google asks these often (they rank high on company frequency lists), but they're easy. Use them as a fast warm-up and aim for about 2 minutes each: say the idea, write the code, give the complexity. Each solution below passed 3+ asserts in scratch.

## 1. LC 1 — Two Sum — ✅ tested
**Idea:** keep a hashmap from value to index; for each x, look up target−x. O(n) time, O(n) space.
```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen: return [seen[target - x], i]
        seen[x] = i
    return []
```
**Google twist:** if the input is sorted, use two pointers for O(1) space. For a stream, store counts so `find(t)` costs O(n) (or keep pair-sums so lookup is O(1) but `add` costs O(n)). For k-sum, sort and recurse down to 2-sum, which is O(n^(k−1)).

## 2. LC 9 — Palindrome Number — ✅ tested
**Idea:** reverse only the back half of the digits and compare it with the front half; there's no string conversion and no overflow. O(log n).
```python
def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0): return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10; x //= 10
    return x == rev or x == rev // 10
```
**Google twist:** "palindrome in base b": use the same loop with `% b`. Or check a linked list: find the middle, reverse the second half, then compare.

## 3. LC 121 + 122 — Best Time to Buy and Sell Stock I & II — ✅ tested
**Idea:** for I (one transaction), track the running minimum and the best `p - min`. For II (unlimited transactions), add up every positive day-to-day difference. Both are O(n) time, O(1) space.
```python
def max_profit(prices):              # LC 121
    lo, best = float('inf'), 0
    for p in prices:
        lo = min(lo, p); best = max(best, p - lo)
    return best

def max_profit2(prices):             # LC 122
    return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))
```
**Google twist:** at most k transactions (LC 188) is a DP over hold/free states, O(nk). With a cooldown or a fee, use a 3-state machine. They may also ask you to return the buy/sell days, not only the profit.

## 4. LC 14 — Longest Common Prefix — ✅ tested
**Idea:** vertical scan: compare column i of the first string against every other string and stop at the first mismatch. O(total chars).
```python
def lcp(strs):
    if not strs: return ""
    for i, ch in enumerate(strs[0]):
        for s in strs[1:]:
            if i == len(s) or s[i] != ch: return strs[0][:i]
    return strs[0]
```
**Google twist:** for many queries against a fixed set, build a trie and walk down while each node has one child. Another option is to sort and compare only the first and last strings.

## 5. LC 13 — Roman to Integer — ✅ tested
**Idea:** if a symbol is smaller than the next one, subtract it; otherwise add it. O(n).
```python
def roman_to_int(s):
    v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and v[ch] < v[s[i+1]]: total -= v[ch]
        else: total += v[ch]
    return total
```
**Google twist:** the reverse direction, Integer to Roman (LC 12), is a greedy pass over a value table that includes 900, 400, 90, 40, 9 and 4. They may also ask you to validate the input, rejecting things like "IIII" or "IC".

## 6. LC 26 + 80 — Remove Duplicates from Sorted Array I & II — ✅ tested
**Idea:** use a write pointer k. Keep x when it differs from `nums[k-1]` (I), or from `nums[k-2]` (II, at most 2 copies). O(n), O(1).
```python
def remove_dups(nums, keep=1):       # keep=1 → LC 26, keep=2 → LC 80
    k = 0
    for x in nums:
        if k < keep or x != nums[k - keep]:
            nums[k] = x; k += 1
    return k
```
**Google twist:** to allow at most m copies, set `keep=m`; the same template works. If the array is unsorted, you need a hash set, or a sort first at O(n log n).

## 7. LC 27 — Remove Element — ✅ tested
**Idea:** write pointer that copies over every x != val. O(n), O(1).
```python
def remove_element(nums, val):
    k = 0
    for x in nums:
        if x != val:
            nums[k] = x; k += 1
    return k
```
**Google twist:** when val is rare and order doesn't matter, swap with the last element and shrink n, which keeps writes to a minimum.

## 8. LC 217 — Contains Duplicate — ✅ tested
**Idea:** compare the set size with the length, or return early on the first repeat using a set. O(n) time, O(n) space.
```python
def contains_dup(nums):
    return len(set(nums)) != len(nums)
```
**Google twist:** "duplicate within distance k" (LC 219) uses a sliding-window set. "Within k indices and value diff ≤ t" (LC 220) uses buckets of width t+1. If memory is O(1), sort first at O(n log n). At massive scale, use a Bloom filter or shard by hash.

## 9. LC 268 — Missing Number — ✅ tested
**Idea:** XOR every index 0..n together with every value; the pairs cancel and the missing number remains. Gauss's sum formula also works. O(n), O(1).
```python
def missing(nums):
    res = len(nums)
    for i, x in enumerate(nums): res ^= i ^ x
    return res
```
**Google twist:** with two numbers missing, the XOR gives a^b; split the set on any set bit. If the input is sorted, binary search for the first i where nums[i] != i. If it's too large for memory, stream it with XOR or a running sum.

## 10. LC 202 — Happy Number — ✅ tested
**Idea:** the digit-square sequence eventually cycles, so use Floyd slow/fast pointers and check whether the cycle contains 1. O(log n) per step, O(1) space.
```python
def is_happy(n):
    def nxt(x): return sum(int(d)**2 for d in str(x))
    slow, fast = n, nxt(n)
    while fast != 1 and slow != fast:
        slow, fast = nxt(slow), nxt(nxt(fast))
    return fast == 1
```
**Google twist:** be ready to explain why it always cycles: numbers with 4+ digits shrink, so the values stay bounded. The same cycle detection applies to any function iteration, as in LC 287 Find Duplicate.

## 11. LC 283 — Move Zeroes — ✅ tested
**Idea:** swap each non-zero into write position k; this keeps the original order. O(n), O(1), with the fewest writes.
```python
def move_zeroes(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]; k += 1
```
**Google twist:** keeping relative order is the constraint, since otherwise two pointers from the ends is enough. To move any predicate-matching elements, this is a stable partition. Expect "minimize writes" as a follow-up.

## 12. LC 344 — Reverse String — ✅ tested
**Idea:** swap in place with two pointers. O(n), O(1).
```python
def reverse_string(s):
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]; i += 1; j -= 1
```
**Google twist:** reverse the words in place (LC 151/186): reverse the whole string, then reverse each word. Another variant reverses only the vowels, or only the letters. Watch out for Unicode grapheme clusters.

## 13. LC 1768 — Merge Strings Alternately — ✅ tested
**Idea:** loop to the longer length and append whichever characters exist. O(m+n).
```python
def merge_alt(w1, w2):
    out = []
    for i in range(max(len(w1), len(w2))):
        if i < len(w1): out.append(w1[i])
        if i < len(w2): out.append(w2[i])
    return "".join(out)
```
**Google twist:** for k strings or iterators, round-robin with a deque of iterators (Zigzag Iterator, LC 281). Build with a list and `join`, not `+=`.

## 14. LC 485 — Max Consecutive Ones — ✅ tested
**Idea:** keep a running count that resets on 0 and track the max. O(n), O(1).
```python
def max_ones(nums):
    best = cur = 0
    for x in nums:
        cur = cur + 1 if x == 1 else 0
        best = max(best, cur)
    return best
```
**Google twist:** "you may flip one 0" (LC 487) or "flip k zeros" (LC 1004) is a sliding window that holds at most k zeros. For a stream with one flip, track the previous run and the current run.

## 15. LC 876 — Middle of the Linked List — ✅ tested
**Idea:** fast moves 2 steps for each slow step; when fast reaches the end, slow is at the middle (the second middle when the length is even). O(n), O(1).
```python
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow
```
**Google twist:** to get the first middle, loop on `fast.next and fast.next.next`. This is the building block for palindrome linked list, reorder list, and merge sort on lists.

## 16. LC 231 — Power of Two — ✅ tested
**Idea:** a power of two has exactly one set bit, so `n & (n-1)` clears it to 0. O(1).
```python
def power_of_two(n):
    return n > 0 and n & (n - 1) == 0
```
**Google twist:** for a power of four, also require the bit to be in an even position: `n & 0x55555555`. For a power of three, check `1162261467 % n == 0`. Counting set bits uses Kernighan's trick, which loops `n &= n-1`.

## 17. LC 58 — Length of Last Word — ✅ tested
**Idea:** scan from the end: skip trailing spaces, then count non-spaces. O(n), O(1). In Python, `len(s.split()[-1])` also works but allocates.
```python
def last_word_len(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ': i -= 1
    j = i
    while j >= 0 and s[j] != ' ': j -= 1
    return i - j
```
**Google twist:** if the input is a stream or a huge file, read backwards in chunks. Clarify whether "word" means split on whitespace or on punctuation too.

## 18. LC 605 — Can Place Flowers — ✅ tested
**Idea:** greedily plant at every 0 whose neighbors are both 0 (or out of bounds). Planting as early as possible is never worse. O(n).
```python
def can_place(bed, n):
    for i in range(len(bed)):
        if bed[i] == 0 and (i == 0 or bed[i-1] == 0) and (i == len(bed)-1 or bed[i+1] == 0):
            bed[i] = 1; n -= 1
    return n <= 0
```
**Google twist:** you can return early once n ≤ 0. If mutating the input isn't allowed, count each zero run: a run of length L fits (L−1)//2 flowers, with edge runs counting as padded. For a circular bed, handle the wraparound neighbor.

## 19. LC 101 — Symmetric Tree — ✅ tested
**Idea:** recursively check that the left subtree mirrors the right one: values are equal, outer pairs match, inner pairs match. O(n) time, O(h) stack.
```python
def is_symmetric(root):
    def mirror(a, b):
        if not a or not b: return a is b
        return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(root.left, root.right) if root else True
```
**Google twist:** the iterative version pushes pairs onto a queue in the order (l.left, r.right), (l.right, r.left). This avoids recursion depth limits on deep trees. A related problem is Same Tree (LC 100) and the N-ary version.
