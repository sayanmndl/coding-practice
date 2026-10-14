# Tier 1 — Matrix simulation, linked lists, math, greedy

Four Tier 1 must-dos: LC 54 Spiral Matrix (+48, +73), LC 2 Add Two Numbers (+19, +141), LC 50 Pow(x, n) (+8 atoi), LC 45 Jump Game II (+55).
Each is a short "do you write clean code under pressure" problem, so the bar is bug-free boundaries and no off-by-ones, not a clever insight.
All solutions were tested in scratch files with python3.

## 1. LC 54 — Spiral Matrix (matrix simulation / boundary shrinking) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Given an m x n matrix, return all of its elements in spiral order (clockwise, starting top-left).
`[[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]`; `[[1,2,3,4],[5,6,7,8],[9,10,11,12]] -> [1,2,3,4,8,12,11,10,9,5,6,7]`.

**Clarify:** Can it be empty? (Yes, return [].) Non-square? (Yes.) Is mutating the input allowed? (Don't.) Is it clockwise from (0,0)? (Yes.)

**Approach:** Brute force: walk with a direction vector and a `visited` grid, turning when you hit a wall or a visited cell. That's O(mn) time and O(mn) extra space. Key insight: keep four boundaries (top, bot, left, right). Do one full layer of four sweeps, shrinking a boundary after each one. Invariant: the unvisited cells are exactly the rectangle [top..bot] x [left..right]. Re-check `top<=bot` / `left<=right` before the bottom and left sweeps so a single leftover row or column isn't emitted twice. O(mn) time, O(1) extra space.
```python
def spiral_order(m: List[List[int]]) -> List[int]:  # O(mn) time, O(1) extra
    if not m or not m[0]:
        return []
    top, bot, left, right = 0, len(m) - 1, 0, len(m[0]) - 1
    out: List[int] = []
    while top <= bot and left <= right:
        for c in range(left, right + 1):
            out.append(m[top][c])
        top += 1
        for r in range(top, bot + 1):
            out.append(m[r][right])
        right -= 1
        if top <= bot:
            for c in range(right, left - 1, -1):
                out.append(m[bot][c])
            bot -= 1
        if left <= right:
            for r in range(bot, top - 1, -1):
                out.append(m[r][left])
            left += 1
    return out
```
**Dry run:** 3x3: top row 1,2,3 (top=1); right col 6,9 (right=1); bottom 8,7 (bot=1); left col 4 (left=1). Layer 2: top row 5 (top=2); the rest are empty ranges, and the guards fail. Result [1,2,3,6,9,8,7,4,5].

**Edge cases & tests:** single row, single column, 1x1, empty, tall 3x2.
```python
assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert spiral_order([[1,2,3]]) == [1,2,3]          # single row: guard stops bottom sweep
assert spiral_order([[1],[2],[3]]) == [1,2,3]      # single col: guard stops left sweep
assert spiral_order([]) == [] and spiral_order([[7]]) == [7]
assert spiral_order([[1,2],[3,4],[5,6]]) == [1,2,4,6,5,3]
```
**Follow-ups:**
- *Spiral Matrix II (generate n x n with 1..n²):* use the same four sweeps, but write instead of read.
- *Counter-clockwise, or start from the center?* Reorder the sweeps. For center-out, reverse the output of the outside-in walk.
- *Huge matrix stored on disk by rows?* A spiral needs random row access. Stream layer by layer and only keep rows `top` and `bot` (plus the boundary columns) in memory.

**Pattern hook:** "traverse/fill a grid in layers" → 4 boundaries + shrink + guard the 3rd and 4th sweeps.

**Sibling: LC 48 Rotate Image (in place, 90° clockwise).** Clockwise rotation = transpose, then reverse each row. Counter-clockwise = transpose, then reverse each column (or reverse rows first, then transpose). O(n²) time, O(1) space. Alternative: 4-way cyclic swap per layer, which has more index math and is easier to get wrong.
```python
def rotate(m: List[List[int]]) -> None:
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):          # j > i: swap each pair once
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for row in m:
        row.reverse()
```

**Sibling: LC 73 Set Matrix Zeroes (O(1) space).** Use row 0 and column 0 as marker arrays. First record whether row 0 and column 0 themselves contain a zero (two booleans). Then mark from the inner cells, zero the inner cells using the markers, and handle row 0 and column 0 last so the markers aren't destroyed early. O(mn) time, O(1) space.
```python
def set_zeroes(m: List[List[int]]) -> None:
    R, C = len(m), len(m[0])
    row0 = any(m[0][c] == 0 for c in range(C))
    col0 = any(m[r][0] == 0 for r in range(R))
    for r in range(1, R):
        for c in range(1, C):
            if m[r][c] == 0:
                m[r][0] = m[0][c] = 0
    for r in range(1, R):
        for c in range(1, C):
            if m[r][0] == 0 or m[0][c] == 0:
                m[r][c] = 0
    if row0:
        for c in range(C): m[0][c] = 0
    if col0:
        for r in range(R): m[r][0] = 0
```

## 2. LC 2 — Add Two Numbers (linked list / dummy head + carry) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Two non-empty linked lists store non-negative integers with their digits in reverse order. Return their sum as a linked list in the same format.
`2->4->3 + 5->6->4 = 7->0->8` (342 + 465 = 807); `9999999 + 9999 = 8->9->9->9->0->0->0->1`.

**Clarify:** Are digits reversed? (Yes, least significant first.) Leading zeros? (None, except the number 0 itself.) Different lengths? (Yes.) Can I allocate new nodes? (Yes.)

**Approach:** Brute force: convert to ints, add, and convert back. Python bigints make that work, but it's O(n) and dodges the point (and overflows in other languages). Optimal: walk both lists together with a carry and append to a dummy head. Loop while `l1 or l2 or carry` so a final carry creates a new node. O(max(m,n)) time, O(1) extra (the output isn't counted).
```python
class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val, self.next = val, next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()              # O(max(m,n)) time, O(1) extra
    carry = 0
    while l1 or l2 or carry:
        s = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        carry, digit = divmod(s, 10)
        tail.next = ListNode(digit)
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

# test helpers
def build(vals: List[int]) -> Optional[ListNode]:
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v); cur = cur.next
    return dummy.next

def to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val); node = node.next
    return out
```
**Dry run:** (2,5)→7 c0; (4,6)→10 → 0 c1; (3,4)+1→8 c0; all are None and carry=0, so stop. Result 7→0→8.

**Edge cases & tests:** the final carry adds a node, unequal lengths, zeros.
```python
A = lambda a, b: to_list(add_two_numbers(build(a), build(b)))
assert A([2,4,3],[5,6,4]) == [7,0,8]
assert A([0],[0]) == [0]
assert A([9,9,9,9,9,9,9],[9,9,9,9]) == [8,9,9,9,0,0,0,1]
assert A([5],[5]) == [0,1]            # carry-only tail node
assert A([1,8],[0]) == [1,8]
```
**Follow-ups:**
- *Digits stored most significant first (LC 445)?* Push both onto stacks (or reverse the lists), add, and prepend each new node to the head.
- *Can't modify or reverse the input, O(1) extra?* Pad the shorter list conceptually by its length difference, then recurse to propagate the carry back. Recursion is O(n) stack.
- *Streams of digits?* LSB-first streams add on the fly with one carry. MSB-first needs buffering, or a count of pending 9s.

**Pattern hook:** building a new list → dummy head + tail pointer; "carry" → loop condition includes `carry`.

**Sibling: LC 19 Remove Nth Node From End.** Two pointers with a gap. Start both at a dummy, move `fast` n+1 steps, then move both until `fast` is None. `slow` now sits just before the target. The dummy handles removing the head. One pass, O(L) time, O(1) space.
```python
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next
```
Tests: `[1,2,3,4,5],2 -> [1,2,3,5]`, `[1],1 -> []`, `[1,2],2 -> [2]` (removes the head).

**Sibling: LC 141 Linked List Cycle.** Floyd's algorithm: slow moves 1 step, fast moves 2. If there is a cycle they must meet, because the gap closes by 1 each step. Otherwise fast hits None. O(n) time, O(1) space (versus a set of visited nodes, which is O(n) space). Follow-up LC 142: after they meet, reset one pointer to head and step both by 1. They meet at the cycle start.
```python
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
```

## 3. LC 50 — Pow(x, n) (math / fast exponentiation) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Implement `pow(x, n)`, i.e. x raised to the integer power n (n can be negative, down to -2³¹).
`pow(2.0, 10) = 1024.0`; `pow(2.0, -2) = 0.25`.

**Clarify:** Can n be negative? (Yes, use 1/x.) Can x be 0 with n<0? (Assume no.) What precision? (Within 1e-5.) Is the `**` builtin allowed? (No.)

**Approach:** Brute force: multiply n times, O(n). With n up to 2³¹ that's too slow. Key insight: binary exponentiation. x^n = (x²)^(n/2), times x if n is odd. Iteratively, scan the bits of n: whenever the low bit is set, multiply it into the result, then square x and shift n. Handle negative n by flipping to 1/x and -n. In Python, -(-2³¹) doesn't overflow. In C++/Java, widen to a long first. O(log n) time, O(1) space.
```python
def my_pow(x: float, n: int) -> float:  # O(log n) time, O(1) space
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
```
**Dry run:** x=2, n=10 (0b1010). Bit0=0: x=4, n=5. Bit=1: res=4, x=16, n=2. Bit=0: x=256, n=1. Bit=1: res=1024, n=0. Returns 1024.

**Edge cases & tests:** n=0, n negative, n=-2³¹, x=0, negative x with odd n.
```python
assert math.isclose(my_pow(2.0, 10), 1024.0)
assert math.isclose(my_pow(2.1, 3), 9.261)
assert math.isclose(my_pow(2.0, -2), 0.25)
assert my_pow(5.0, 0) == 1.0 and my_pow(0.0, 5) == 0.0
assert math.isclose(my_pow(1.0, -2**31), 1.0)     # INT_MIN exponent
assert math.isclose(my_pow(-2.0, 3), -8.0)
```
**Follow-ups:**
- *Modular power (x^n mod m) for huge n?* Use the same loop and take `% m` after each multiply (that's Python's `pow(x, n, m)`). It's the basis of RSA and of modular inverses via Fermat.
- *Matrix power?* The same algorithm on 2x2 matrices gives Fibonacci in O(log n), and in general linear recurrences in O(k³ log n).
- *Recursive version?* `half = pow(x, n//2); return half*half*(x if n odd else 1)`. That's O(log n) stack. Never call pow(x, n//2) twice, or it becomes O(n).

**Pattern hook:** "n up to 1e9 / 2³¹ and a repeated associative operation" → square-and-multiply on the bits of n.

**Sibling: LC 8 String to Integer (atoi).** Scan in order: skip leading spaces, take an optional single sign, then read digits until the first non-digit. Clamp to [-2³¹, 2³¹-1]. Check for overflow *before* multiplying: if `num > (INT_MAX - d) // 10`, clamp. The same check covers INT_MIN, because the magnitude limit for negatives is INT_MAX+1, and any magnitude ≥ INT_MAX+1 clamps to INT_MIN anyway. Edge cases: `""`, `"   "`, `"+"`, `"+-12"` → 0, `"0-1"` → 0, `"words 987"` → 0, leading zeros, and the boundary values. O(n) time, O(1) space.
```python
def my_atoi(s: str) -> int:
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    i, n = 0, len(s)
    while i < n and s[i] == ' ':
        i += 1
    sign = 1
    if i < n and s[i] in '+-':
        sign = -1 if s[i] == '-' else 1
        i += 1
    num = 0
    while i < n and s[i].isdigit():
        d = ord(s[i]) - ord('0')
        if num > (INT_MAX - d) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        num = num * 10 + d
        i += 1
    return sign * num
```
Tests: `"42"→42`, `"   -042"→-42`, `"1337c0d3"→1337`, `"+-12"→0`, `"2147483648"→2147483647`, `"-2147483648"→-2147483648`, `"-2147483649"→-2147483648`, `"-91283472332"→INT_MIN`.

## 4. LC 45 — Jump Game II (greedy / implicit BFS levels) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** `nums[i]` is the maximum jump length from index i. Starting at index 0, return the minimum number of jumps to reach the last index (it's guaranteed reachable).
`[2,3,1,1,4] -> 2` (0→1→4); `[2,3,0,1,4] -> 2`.

**Clarify:** Is the last index always reachable? (Yes; otherwise return -1.) Is a single element 0 jumps? (Yes.) Non-negative values? (Yes.) Do we need the path or just the count? (Just the count.)

**Approach:** Brute force: DP `dp[j] = min(dp[i]+1)` over every i that can reach j, which is O(n²). Or a BFS over indices, O(n²) edges. Key insight: the BFS levels are contiguous index ranges. Level k = the indices reachable in exactly k jumps = (end of the previous level, `cur_end`]. Sweep i, tracking `farthest = max(i + nums[i])`. When i reaches `cur_end`, the current level is exhausted: jump once and set `cur_end = farthest`. Loop only to n-2, since standing on the last index needs no further jump. O(n) time, O(1) space.
```python
def jump(nums: List[int]) -> int:  # O(n) time, O(1) space
    jumps, cur_end, farthest = 0, 0, 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:              # finished scanning this BFS level
            jumps += 1
            cur_end = farthest
            if cur_end >= len(nums) - 1:
                break
    return jumps
```
**Dry run:** [2,3,1,1,4]. i=0: far=2, i==end → jumps=1, end=2. i=1: far=4. i=2: far=4, i==end → jumps=2, end=4 ≥ 4, break. Returns 2.

**Edge cases & tests:** a single element, all ones, a first jump that covers everything, a zero inside.
```python
assert jump([2,3,1,1,4]) == 2
assert jump([2,3,0,1,4]) == 2
assert jump([0]) == 0                  # already at end
assert jump([1,2]) == 1
assert jump([1,1,1,1]) == 3
assert jump([10,1,1,1]) == 1
```
**Follow-ups:**
- *Unreachable possible?* If `i == cur_end` and `farthest <= i`, you're stuck: return -1.
- *Return the actual path?* Within each level, remember which i achieved `farthest` (a parent pointer). Alternatively run an explicit BFS with parents.
- *Jumps both directions / exact jump lengths (LC 1306, 1345)?* The graph is no longer interval-shaped, so do a real BFS with a visited set, O(n + edges).

**Pattern hook:** "min steps where each position reaches a contiguous range" → greedy BFS by level windows (`cur_end`, `farthest`).

**Sibling: LC 55 Jump Game (can you reach the end?).** Track the max reachable index. If you ever stand at i > reach, you're stuck. Otherwise extend reach with `i + nums[i]`. Equivalent: scan backward, moving a "goal" to i whenever `i + nums[i] >= goal`, and check `goal == 0`. O(n) time, O(1) space.
```python
def can_jump(nums: List[int]) -> bool:
    reach = 0
    for i, v in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + v)
    return True
```
Tests: `[2,3,1,1,4]→True`, `[3,2,1,0,4]→False`, `[0]→True`, `[0,1]→False`, `[2,0,0]→True`.
