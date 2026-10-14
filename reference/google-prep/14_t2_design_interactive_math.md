# Tier 2 — Design classes, interactive, overflow math

Problems (all **Tier 2**): 1. LC 2034 Stock Price Fluctuation (design + lazy-deletion heaps) · 2. LC 1146 Snapshot Array (versioned design + bisect) · 3. LC 843 Guess the Word (interactive API + minimax elimination) · 4. LC 7 Reverse Integer (32-bit overflow math; LC 29 as follow-up).
All solutions were tested in scratch files against randomized brute-force references.

## 1. LC 2034 — Stock Price Fluctuation (hashmap + two heaps, lazy deletion) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** You get a stream of `(timestamp, price)` records, possibly out of order. A later record for the same timestamp *corrects* the earlier one. Support `update(ts, price)`, `current()` (the price at the latest timestamp), `maximum()`, and `minimum()` over the current (corrected) prices.
Example: `update(1,10), update(2,5)` → `current()=5, maximum()=10`; `update(1,3)` → `maximum()=5`; `update(4,2)` → `minimum()=2`.

**Clarify:** Can timestamps arrive out of order? *Yes.* Will the queries ever run on an empty structure? *No, there's always at least one update first.* Up to 1e5 operations? *Yes.* Do corrections dominate? *Assume a mix.*

**Approach:** Brute force: a dict plus a scan of `max(values)` gives O(n) per query. Key insight: a correction makes an old heap entry *stale*, but we don't need to remove it right away. Store `(price, ts)` in a min-heap and a max-heap. On a query, pop from the top while `price != current_price[ts]` (lazy deletion). Invariant: the heap top is valid once those pops finish. Each pushed entry is popped at most once, so cost is amortized O(log n). Alternative: a `SortedList` of prices (or a TreeMap of price→count) gives O(log n) worst case, but there's no SortedList on the Chromebook.
```python
import heapq
class StockPrice:
    def __init__(self) -> None:
        self.price: dict[int, int] = {}          # timestamp -> latest price
        self.latest = 0
        self.maxh: list[tuple[int, int]] = []    # (-price, ts)
        self.minh: list[tuple[int, int]] = []    # (price, ts)

    def update(self, timestamp: int, price: int) -> None:   # O(log n)
        self.price[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.maxh, (-price, timestamp))
        heapq.heappush(self.minh, (price, timestamp))

    def current(self) -> int:                                # O(1)
        return self.price[self.latest]

    def maximum(self) -> int:                                # amortized O(log n)
        while -self.maxh[0][0] != self.price[self.maxh[0][1]]:
            heapq.heappop(self.maxh)                         # stale entry
        return -self.maxh[0][0]

    def minimum(self) -> int:
        while self.minh[0][0] != self.price[self.minh[0][1]]:
            heapq.heappop(self.minh)
        return self.minh[0][0]
```
*Complexity:* update O(log n); current O(1); max/min amortized O(log n). Space O(total updates), because stale entries stay in the heaps.

**Dry run:** After `update(1,10), update(2,5)`, maxh = [(-10,1), (-5,2)]. Then `update(1,3)` sets price[1]=3 and pushes (-3,1). `maximum()`: the top is (-10,1), and 10 ≠ price[1]=3, so pop it. The new top is (-5,2), which is valid, so return 5.

**Edge cases & tests:** a correction of the only point; out-of-order timestamps (current = max ts, not the last update); the same price at two timestamps (the stale check is by ts, so this is fine).
```python
s = StockPrice(); s.update(1,10); s.update(2,5)
assert s.current()==5 and s.maximum()==10
s.update(1,3); assert s.maximum()==5 and s.minimum()==3
s2 = StockPrice(); s2.update(7,1); s2.update(7,9); assert s2.minimum()==9
s3 = StockPrice(); s3.update(5,50); s3.update(2,20); assert s3.current()==50
```
**Follow-ups:**
- *What if heap memory blows up because of many corrections?* Rebuild a heap once it holds more than 2× as many entries as the dict (O(n) heapify), or switch to a balanced BST / SortedList of (price, ts) with a true delete.
- *What about the max over a sliding time window?* Use a monotonic deque if timestamps arrive in order. Otherwise use a segment tree over the timestamps.
- *Is it thread-safe?* Use a single lock around update and the queries. The lazy pops mutate state, so even the "reads" need the lock.

**Pattern hook:** "max/min with updates or deletes, and no SortedList" → heap + a source-of-truth map + lazy deletion on peek.

## 2. LC 1146 — Snapshot Array (per-index version list + binary search) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** Implement `SnapshotArray(length)`, which starts as all zeros. It supports `set(index, val)`; `snap()`, which returns the snap id (`0, 1, 2, ...`); and `get(index, snap_id)`, the value at `index` when that snap was taken.
Example: `set(0,5); snap()→0; set(0,6); get(0,0)→5`.

**Clarify:** Is length up to 5e4, with up to 5e4 calls total? *Yes.* Will `snap_id` passed to `get` always be one that has been taken? *Yes.* Are reads or writes heavier? *Assume a mix, with many snaps that have few changes.* Can multiple sets happen to the same index between snaps? *Yes, and the last one wins.*

**Approach:** Brute force: copy the whole array on every snap, so snap is O(n) time and O(n·S) memory, which is 2.5e9 cells at the worst case. That's a TLE/MLE. Key insight: store *changes* only. For each index, keep a sorted list of `(snap_id, val)` for the snaps in which it was written. `get(i, s)` = the value of the last entry with `snap_id ≤ s`, found by `bisect_right(ids, s) - 1`. Invariant: `ids[i]` is strictly increasing and starts with the sentinel `(0, 0)`. A write within the same snap overwrites the last entry instead of appending, so there's at most one entry per (index, snap).
```python
from bisect import bisect_right
class SnapshotArray:
    def __init__(self, length: int) -> None:
        self.snap_id = 0
        self.ids: list[list[int]] = [[0] for _ in range(length)]   # snap ids written
        self.vals: list[list[int]] = [[0] for _ in range(length)]  # parallel values

    def set(self, index: int, val: int) -> None:           # O(1)
        if self.ids[index][-1] == self.snap_id:
            self.vals[index][-1] = val                      # overwrite within same snap
        else:
            self.ids[index].append(self.snap_id)
            self.vals[index].append(val)

    def snap(self) -> int:                                  # O(1)
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:         # O(log S_i)
        i = bisect_right(self.ids[index], snap_id) - 1      # last write at or before snap_id
        return self.vals[index][i]
```
*Complexity:* set O(1), snap O(1), get O(log k), where k is the number of writes to that index. Space O(n + distinct (index, snap) writes).

**Memory trade-offs (say this out loud):**
- **Copy-per-snap:** O(1) get, but O(n) per snap. This only wins if nearly every index changes between snaps.
- **Version lists (above):** memory is proportional to the number of *changes*. The `[0]` sentinel per index costs O(n) upfront. Make it lazy (a dict of index → lists, created on the first set) if the array is huge and sparse.
- **Parallel lists vs list of tuples:** parallel int lists are friendlier to bisect (no tuple comparisons, no `key=`) and lighter than tuple objects. In production, use `array('i')` for compactness.
- **Dict per snap (diff only), with get walking backward:** O(1) set, but get is O(S) worst case. Version lists are better.
- **Persistent segment tree:** O(log n) per set with structural sharing, and it supports range queries on old versions. That's overkill unless asked.

**Dry run:** `set(0,5)` → ids[0]=[0], vals[0]=[5] (overwrites the sentinel, since snap_id is 0). `snap()`→0. `set(0,6)` → ids[0]=[0,1], vals[0]=[5,6]. `get(0,0)`: bisect_right([0,1],0)=1, so i=0 → 5.

**Edge cases & tests:** an index never set (sentinel → 0); several sets within one snap; snaps with no changes in between; get on the latest snap.
```python
a = SnapshotArray(3); a.set(0,5); assert a.snap()==0; a.set(0,6)
assert a.get(0,0)==5 and a.get(1,0)==0
a.set(2,1); a.set(2,4); a.snap(); a.snap()
assert a.get(2,2)==4 and a.get(2,1)==0 and a.get(2,3)==4
assert len(a.ids[2])==2   # one entry per (index, snap)
```
**Follow-ups:**
- *What if many snaps are taken but each touches few indices?* That's exactly the case this design handles: memory stays proportional to the writes.
- *What if the history is too big for memory?* Use an LSM-style approach: keep the recent versions in memory and flush older `(index, snap)→val` runs to sorted files. get then does a binary search per level. This is MVCC in databases.
- *What about a "delete old snapshots" (GC) operation?* Track the minimum live snap, and for each index drop all entries before the last one ≤ that minimum.

**Pattern hook:** "query the state at time/version t" → store a per-key sorted change log and binary search for the floor (Time Based Key-Value Store, LC 981, is the same pattern).

## 3. LC 843 — Guess the Word (interactive, minimax candidate elimination) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** You're given a list of unique 6-letter `words`, one of which is the secret. You can call `master.guess(word)`, which returns the number of exact position matches with the secret (or -1 if the word isn't in the list). Find the secret within `allowedGuesses` (classically 10).
Example: words=`["acckzz","ccbazz","eiowzz","abcczz"]`, secret=`"acckzz"`: `guess("aaaaaa")→-1`, `guess("ccbazz")→3`, `guess("acckzz")→6`.

**Clarify:** Are the words all length 6 and distinct? *Yes.* Is the API's only feedback the match count? *Yes.* Is the guess budget fixed? *Yes, about 10.* Is the secret guaranteed to be in the list? *Yes.*

**Approach:** Brute force: guess the words one by one, which can take n guesses. Key insight: after guessing `g` and getting `m`, the secret must satisfy `match(w, g) == m`, so filter the candidates down to those. Invariant: the secret is always among the candidates. To guarantee progress, pick the guess that minimizes the **largest** bucket of `match(g, ·)` over the remaining candidates (minimax). The "most common match" heuristic is related: avoid guesses whose likely answer is 0, because the 0-bucket is usually huge. Each round costs O(n²·6), and there are ≤10 rounds.
```python
from collections import Counter

def match(a: str, b: str) -> int:
    return sum(x == y for x, y in zip(a, b))

def findSecretWord(words: list[str], master: "Master") -> None:
    cands = list(dict.fromkeys(words))
    while cands:
        def worst(w: str) -> int:   # size of the largest bucket if we guess w
            return max(Counter(match(w, o) for o in cands).values())
        g = min(cands, key=worst)                 # minimax guess, O(n^2)
        m = master.guess(g)
        if m == 6:
            return
        cands = [w for w in cands if match(w, g) == m]
```
*Complexity:* O(G · n² · L) time, with G ≤ 10 guesses and L = 6. O(n) space.

**Mock Master for tests (interactive problems: always build this):**
```python
class Master:
    def __init__(self, words, secret, allowed=10):
        self.words, self.secret, self.allowed = set(words), secret, allowed
        self.calls, self.found = 0, False
    def guess(self, word: str) -> int:
        self.calls += 1
        if word not in self.words: return -1
        m = match(word, self.secret); self.found |= (m == 6); return m
```
**Dry run:** With the 4-word example, the buckets are: `acckzz` → {6,3,2,4}, all of size 1 (worst = 1); `ccbazz` → {2:2} (worst = 2); `eiowzz` → {2:3}; `abcczz` → {2:2}. The minimax pick is `"acckzz"`, the guess returns 6, and we're done. If the secret were `"ccbazz"`: the guess returns 3, and the only candidate with match 3 to `acckzz` is `ccbazz`, so the next guess finds it.

**Edge cases & tests:** a single word; two words; a small alphabet (where words share many letters, the adversarial case); a check that the guess count stays ≤ allowed.
```python
ws=["acckzz","ccbazz","eiowzz","abcczz"]; M=Master(ws,"acckzz")
findSecretWord(ws,M); assert M.found and M.calls<=10
M=Master(["abcdef"],"abcdef"); findSecretWord(["abcdef"],M); assert M.calls==1
assert match("abcdef","abcxyz")==3
# randomized: 300 trials of 100 words over {abc},{abcd},{a-z}: always found, worst = 10 calls
```
**Follow-ups:**
- *Why not guess randomly?* Random guessing works on average, but an adversarial test set (words sharing 0 matches) can blow the budget. Minimax gives a worst-case guarantee per round.
- *What if n is large (e.g. 1e4)?* O(n²) per round is too slow. Sample about 100 candidates to evaluate as guesses, or use the per-position letter-frequency score: pick the word maximizing Σ freq[pos][char], which is O(n·L).
- *Can we guess words outside the candidate set?* In Wordle-style variants, yes: a non-candidate can split better. Evaluate all words as guesses but score them against the candidates.

**Pattern hook:** "an oracle returns a similarity score, with limited queries" → keep a consistent candidate set and choose the query that minimizes the worst-case remaining set (a minimax / decision-tree split).

## 4. LC 7 — Reverse Integer (digit math, 32-bit overflow guard) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** Reverse the digits of a signed 32-bit integer `x`. If the result falls outside `[-2^31, 2^31-1]`, return 0. **Assume the environment can't store 64-bit integers.**
Examples: `123→321`, `-123→-321`, `120→21`, `1534236469→0`.

**Clarify:** Is it truncated with the sign kept? *Yes.* Do trailing zeros vanish? *Yes.* Is a string reversal allowed? *Not here: the point is the arithmetic and the overflow check.* Should Python's big ints be treated as 32-bit? *Yes, so never compute an out-of-range intermediate value.*

**Approach:** Brute force: `int(str(abs(x))[::-1])` and then a range check. That relies on the intermediate fitting in 64 bits (or a big int). Key insight: pop digits with `% 10` and push them with `res*10 + d`, but **check before multiplying**: overflow happens iff `res > MAX//10`, or `res == MAX//10` and `d > 7` (since MAX = 2147483647). Symmetrically, the negative side underflows iff `res < -214748364`, or it equals that and `d < -8` (MIN = -2147483648). The res and digit signs match the sign of x, so we never take `abs(INT_MIN)`, which itself overflows. In Python, `x % -10` emulates C's truncated remainder for negative x.
```python
INT_MAX, INT_MIN = 2**31 - 1, -2**31

def reverse(x: int) -> int:
    res = 0
    while x != 0:
        d = x % 10 if x >= 0 else x % -10      # C-style remainder: sign follows x
        x = (x - d) // 10                      # exact division, truncates toward 0
        if res > INT_MAX // 10 or (res == INT_MAX // 10 and d > 7):
            return 0
        if res < -(INT_MAX // 10) or (res == -(INT_MAX // 10) and d < -8):
            return 0
        res = res * 10 + d                     # safe: checked before multiplying
    return res
```
*Complexity:* O(log₁₀|x|) = O(10) time, O(1) space.

**Dry run:** x=-123: d=-3, x=-12, res=-3 → d=-2, x=-1, res=-32 → d=-1, x=0, res=-321. ✓
x=1534236469: after 9 digits, res=964632435 > 214748364, so the check fires before the 10th push → return 0.

**Edge cases & tests:** 0; trailing zeros; INT_MAX and INT_MIN (both reverse to an overflow); near-boundary values that just fit; random values vs a string reference (100k cases).
```python
assert reverse(123)==321 and reverse(-123)==-321 and reverse(120)==21
assert reverse(0)==0 and reverse(1534236469)==0
assert reverse(INT_MAX)==0 and reverse(INT_MIN)==0
assert reverse(1463847412)==2147483641 and reverse(-1463847412)==-2147483641
```
Note: since the input is itself 32-bit, a 10-digit x must start with 1 or 2, so the reversed last digit d is ≤ 2 and the `d > 7` clause never actually fires. Still say it: it's the general guard (it matters in LC 8 atoi).

**Follow-ups:**
- *LC 29 Divide Two Integers (no `*`, `/`, `%`; 32-bit only):* handle the single overflow case `INT_MIN / -1 → INT_MAX` first. Work in **negatives**, because |INT_MIN| doesn't fit as a positive. Repeatedly double the divisor (`t += t`, guarded by `t >= INT_MIN >> 1`) while it still fits inside the dividend, then subtract and add the multiplier. That's O(log² n), or O(log n) with a precomputed doubling table. Tested:
```python
def divide(dividend: int, divisor: int) -> int:
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    neg = (dividend < 0) != (divisor < 0)
    a, b, q = -abs(dividend), -abs(divisor), 0   # negatives: |INT_MIN| fits
    while a <= b:
        t, k = b, 1
        while t >= INT_MIN >> 1 and a <= t + t:   # double without overflow
            t += t; k += k
        a -= t; q += k
    return -q if neg else q
```
- *LC 8 String to Integer (atoi):* the same pre-multiply guard, but clamp to MAX/MIN instead of returning 0.
- *What about 64-bit or arbitrary width?* Parameterize MAX/MIN. The guard `res > MAX//10 or (== and d > MAX%10)` generalizes.

**Pattern hook:** "no 64-bit / detect overflow" → compare against `LIMIT // 10` (and the last digit) *before* the `*10 + d` step. For division, work in the negative domain.
