# Backtracking & ML-flavoured coding — Google style

Two gaps in the revision cards. **Part A** is three backtracking problems not already in `google_coding_index.md`. N-Queens and Word Search II are both carded already, so Sudoku Solver (bitmasks + MRV pruning) fills the pruning slot. **Part B** is four ML-flavoured coding problems that are plausible for an ML SWE on Gemini: attention, decoding/sampling, BPE, and ranking metrics. Each solution is ≤40 lines.

Every solution was run against 5+ asserts, and most also against a brute-force oracle with randomized inputs. Test files live in `scratchpad/coding_bt_ml/p1–p7.py`.

**Backtracking template to say out loud:** state → choices → prune → do / recurse / undo. To dedupe, sort the input and skip `nums[i] == nums[i-1]` at the same depth.

---

# Part A — Backtracking

## 1. Combination Sum II (+ Permutations II) (backtracking, dedupe by sort + skip) — Medium ✅ tested
**Prompt (as asked):** Given candidates (they may contain duplicates) and a target, return all *unique* combinations that sum to the target. Each element can be used at most once.
Example: `[10,1,2,7,6,1,5], 8 → [[1,1,6],[1,2,5],[1,7],[2,6]]`.

**Clarify:** Are the numbers positive? (Yes, which enables the `break` prune.) Does output order matter? (No.) Is an empty list a valid answer for target 0? (Yes, `[[]]`.) What sizes? (n ≤ 100, target ≤ 30.)

**Approach:** Brute force enumerates all 2^n subsets and dedupes them with a set of tuples: O(2^n · n) time plus the hashing. The key insight is to **sort**, so that duplicates sit next to each other. At a given recursion depth, picking the second `1` produces the same subtrees as picking the first, so skip `i > start and c[i] == c[i-1]`. Because the input is sorted, `c[i] > remain` lets you `break`. Worst case is O(2^n · n), but the search is output-sensitive in practice. Space is O(n) recursion depth.
```python
def combination_sum2(cands: List[int], target: int) -> List[List[int]]:
    cands = sorted(cands)
    res: List[List[int]] = []
    path: List[int] = []

    def bt(start: int, remain: int) -> None:
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(cands)):
            if i > start and cands[i] == cands[i - 1]:
                continue                      # same value already tried at this depth
            if cands[i] > remain:
                break                         # sorted => all later ones too big
            path.append(cands[i])
            bt(i + 1, remain - cands[i])      # i+1: each element used at most once
            path.pop()

    bt(0, target)
    return res
```
**Permutations II variant.** There is no `start` index here, so dedupe with a `used[]` array instead. Only use an equal copy when its left twin is already in the path:
```python
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue                      # only use equal copies left-to-right
```
**Dry run:** sorted = `[1,1,2,5,6,7,10]`. At depth 0 the first `1` is taken, giving `[1,1,6]`, `[1,2,5]`, `[1,7]`. The second `1` at depth 0 is skipped. `2` gives `[2,6]`. `5` with remaining 3 hits `6 > 3`, so it breaks.

**Edge cases & tests:** empty input, target 0, all duplicates, no solution. Both functions were also fuzzed against `itertools` brute force (400 cases).
```python
assert combination_sum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
assert combination_sum2([2,5,2,1,2], 5) == [[1,2,2],[5]]
assert combination_sum2([], 3) == [] and combination_sum2([3], 0) == [[]]
assert combination_sum2([1,1,1,1], 2) == [[1,1]]
assert permute_unique([1,1,2]) == [[1,1,2],[1,2,1],[2,1,1]]
```
**Follow-ups:**
- *Count only, no list:* use 0/1-knapsack DP over a value→multiplicity map. Number of ways = DP over distinct values with bounded counts, O(distinct · target · maxcount).
- *Negative numbers:* the `break` prune is no longer valid, and the search may never terminate if reuse is allowed. Bound it by length, or use meet-in-the-middle.
- *Huge output:* make it a generator (`yield`) so the caller can stream results.

**Pattern hook:** "all unique combos/perms with duplicates in the input" → sort, then skip equal neighbours at the same depth.

## 2. Sudoku Solver (backtracking + bitmask pruning + MRV) — Hard ✅ tested
*(N-Queens and Word Search II are already in the index, so this is the pruning problem instead.)*

**Prompt (as asked):** Fill a 9×9 board (`'.'` = empty) in place so that every row, column and 3×3 box contains 1–9 exactly once. Return whether it was solvable.

**Clarify:** Is a unique solution guaranteed? (Assume no; return False if unsolvable.) Can the givens be invalid? (Detect them and return False.) In place or a copy? (In place.) Generalize to N²×N²? (Mention it as a follow-up.)

**Approach:** Brute force tries 9 digits in each empty cell in row-major order and checks validity by scanning, so each check is O(27) inside a 9^E tree. Improvements:
1. **Bitmasks.** `rows[r] | cols[c] | boxes[b]` gives the used digits in O(1). Then `free = ~used & 0x1FF`, and you iterate set bits with `free & -free`.
2. **MRV (most-constrained cell first).** Always branch on the empty cell with the fewest candidates. A 0-candidate cell fails immediately, and a 1-candidate cell is a forced move. This turns the "world's hardest" puzzles into milliseconds.

Worst case is still exponential, but the branching factor collapses. Space is O(81).
```python
def solve_sudoku(board: List[List[str]]) -> bool:
    rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9   # bit d set => digit d+1 used
    empties = []
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                empties.append((r, c))
            else:
                bit = 1 << (int(board[r][c]) - 1)
                b = (r // 3) * 3 + c // 3
                if (rows[r] | cols[c] | boxes[b]) & bit:
                    return False                    # invalid given
                rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit

    def bt() -> bool:
        if not empties:
            return True
        # MRV: pick the empty cell with the fewest legal digits
        k = min(range(len(empties)), key=lambda j: bin(
            ~(rows[empties[j][0]] | cols[empties[j][1]] |
              boxes[empties[j][0] // 3 * 3 + empties[j][1] // 3]) & 0x1FF).count('1'))
        empties[k], empties[-1] = empties[-1], empties[k]
        r, c = empties.pop()
        b = r // 3 * 3 + c // 3
        free = ~(rows[r] | cols[c] | boxes[b]) & 0x1FF
        while free:
            bit = free & -free                      # lowest set bit
            free ^= bit
            rows[r] ^= bit; cols[c] ^= bit; boxes[b] ^= bit
            board[r][c] = str(bit.bit_length())
            if bt():
                return True
            rows[r] ^= bit; cols[c] ^= bit; boxes[b] ^= bit
        board[r][c] = '.'
        empties.append((r, c))
        return False

    return bt()
```
**Dry run:** On the LeetCode board, MRV first finds cells with exactly one candidate and fills them as forced moves, much like naked singles. Branching only happens once no forced cell remains. Row 0 ends as `534678912`.

**Edge cases & tests:** the LC example, the "world's hardest" (Inkala) puzzle, an empty board, duplicate givens, a locally consistent but unsolvable board, and an already-solved board.
```python
b = parse(lc); assert solve_sudoku(b) and valid(b) and ''.join(b[0]) == "534678912"
b = parse(hard); assert solve_sudoku(b) and valid(b)
b = parse("."*81); assert solve_sudoku(b) and valid(b)
assert solve_sudoku(parse("55" + "."*79)) is False
assert solve_sudoku(parse("12345678." + "........9" + "."*63)) is False
```
**Follow-ups:**
- *Count solutions / check uniqueness:* don't return on the first success. Count, and stop at 2.
- *Faster:* add constraint propagation (after each placement, propagate naked/hidden singles), or use Knuth's Algorithm X / Dancing Links, since Sudoku is an exact cover problem.
- *N²×N² boards:* the same code works with N² bits per mask. MRV becomes essential.

**Pattern hook:** "fill a grid under all-different constraints" → bitmask feasibility + most-constrained-variable-first backtracking.

## 3. Expression Add Operators (backtracking with running value) — Hard ✅ tested
**Prompt (as asked):** Given a digit string `num` and an integer `target`, insert `+`, `-`, `*` between digits (or nothing, to concatenate) so that the expression evaluates to `target`. Return all such expressions.
Examples: `"123", 6 → ["1+2+3","1*2*3"]`; `"105", 5 → ["1*0+5","10-5"]`.

**Clarify:** Are leading zeros like `"05"` allowed? (No, but `"0"` alone is fine.) Is unary minus allowed? (No.) What length? (≤10 digits.) Can values overflow? (Python ints are unbounded; in C++/Java use long.)

**Approach:** Brute force generates all 4^(n-1) operator strings, then `eval`s each one: O(4^n · n). The insight is to evaluate **incrementally** while you build. Track `value` (the total so far) and `last` (the signed last multiplicative term). `*` has higher precedence, so to append `* x` you undo the last term and redo it multiplied:
$$value' = value - last + last \cdot x,\qquad last' = last \cdot x$$
This makes each extension O(1) on the arithmetic, so the total is O(4^n · n), with the n coming from string building. Recursion depth is O(n).
```python
def add_operators(num: str, target: int) -> List[str]:
    res: List[str] = []

    def bt(i: int, expr: str, value: int, last: int) -> None:
        # value = result of expr so far; last = signed last multiplicative term
        if i == len(num):
            if value == target:
                res.append(expr)
            return
        for j in range(i, len(num)):
            if j > i and num[i] == '0':
                break                                   # no multi-digit operand with leading 0
            s = num[i:j + 1]
            x = int(s)
            if i == 0:
                bt(j + 1, s, x, x)
            else:
                bt(j + 1, expr + '+' + s, value + x, x)
                bt(j + 1, expr + '-' + s, value - x, -x)
                # undo last term, re-apply it multiplied by x (precedence)
                bt(j + 1, expr + '*' + s, value - last + last * x, last * x)

    if num:
        bt(0, '', 0, 0)
    return res
```
**Dry run** (`"232"`, 8): `2` → `2+3` (value 5, last 3) → `2+3*2`: value = 5−3+3·2 = 8 ✓. And `2*3` (value 6, last 6) → `2*3+2` = 8 ✓.

**Edge cases & tests:** leading zeros, `"00"`, a single digit, empty input, no solution. Also fuzzed against an `eval` oracle (200 cases).
```python
assert sorted(add_operators("123", 6)) == ["1*2*3", "1+2+3"]
assert sorted(add_operators("232", 8)) == ["2*3+2", "2+3*2"]
assert sorted(add_operators("105", 5)) == ["1*0+5", "10-5"]
assert sorted(add_operators("00", 0)) == ["0*0", "0+0", "0-0"]
assert add_operators("3456237490", 9191) == [] and add_operators("", 0) == []
```
**Follow-ups:**
- *Add division:* integer division breaks the `last` trick because results get truncated. Keep exact fractions with `fractions.Fraction`, or restrict to exact divisions.
- *Count only, or just check existence:* prune is hard because `*` makes values non-monotonic. Memoization on `(i, value, last)` can help for counting, but the state space is large.
- *Faster string building:* keep a list `path` with append/pop and `''.join` only at the leaves. This avoids O(n) concatenation per call.

**Pattern hook:** "insert operators / partition a string and evaluate" → carry (value, last operand) so precedence is O(1) to undo.

---

# Part B — ML-flavoured coding (NumPy)

Format: Clarify → Approach (math) → code → tests → follow-ups.

## 4. Causal multi-head self-attention forward + stable softmax (NumPy) — Medium ✅ tested
**Prompt (as asked):** Implement the forward pass of multi-head self-attention with a causal mask, given `x: (B,T,D)` and projections `Wq, Wk, Wv, Wo: (D,D)`. Write your own numerically stable softmax.

**Clarify:** Are there biases? (No.) Is there a padding mask too? (No, causal only, but say how you'd add one.) Training or inference? (Forward only.) Is `D` divisible by `H`? (Yes, assert it.)

**Approach:**
- Per head: $\mathrm{Attn}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_h}} + M\right)V$, with $M_{ij}=-\infty$ for $j>i$.
- Stable softmax: $\mathrm{softmax}(z)_i = \frac{e^{z_i-m}}{\sum_j e^{z_j-m}}$ with $m=\max_j z_j$. This is shift-invariant and never overflows. Guard fully masked rows so that $-\infty-(-\infty)$ does not produce NaN.
- Split heads with reshape `(B,T,H,d_h)` → transpose to `(B,H,T,d_h)`, so the matmuls batch over B and H.
- Cost: O(B·T²·D) time and O(B·H·T²) memory for the scores. The $\sqrt{d_h}$ scaling keeps the logit variance around 1, so the softmax doesn't saturate.
```python
def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    m = np.max(x, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0.0)             # fully-masked row: avoid inf - inf
    e = np.exp(x - m)
    s = np.sum(e, axis=axis, keepdims=True)
    return e / np.where(s == 0, 1.0, s)              # fully-masked row -> zeros, not NaN

def mha_forward(x: np.ndarray, Wq: np.ndarray, Wk: np.ndarray, Wv: np.ndarray,
                Wo: np.ndarray, n_heads: int, causal: bool = True) -> np.ndarray:
    """x: (B, T, D); W*: (D, D). Returns (B, T, D)."""
    B, T, D = x.shape
    assert D % n_heads == 0
    hd = D // n_heads

    def split(t: np.ndarray) -> np.ndarray:          # (B,T,D) -> (B,H,T,hd)
        return t.reshape(B, T, n_heads, hd).transpose(0, 2, 1, 3)

    q, k, v = split(x @ Wq), split(x @ Wk), split(x @ Wv)
    scores = q @ k.transpose(0, 1, 3, 2) / np.sqrt(hd)       # (B,H,T,T)
    if causal:
        mask = np.triu(np.ones((T, T), dtype=bool), k=1)     # True = future
        scores = np.where(mask, -np.inf, scores)
    attn = softmax(scores, axis=-1)
    out = attn @ v                                           # (B,H,T,hd)
    out = out.transpose(0, 2, 1, 3).reshape(B, T, D)         # merge heads
    return out @ Wo
```
**Tests:**
```python
s = softmax(np.array([[1000., 1001., 1002.]]))
assert np.all(np.isfinite(s)) and np.isclose(s.sum(), 1)                # no overflow
assert np.allclose(softmax(np.array([[-np.inf, -np.inf]])), 0)          # no NaN
assert np.allclose(out, ref_loop)          # matches naive per-head / per-position loop
x2 = x.copy(); x2[:, 3:] += 10.0           # causality: future edits don't leak back
assert np.allclose(out[:, :3], mha_forward(x2, *Ws, n_heads=H)[:, :3])
assert np.allclose(mha_forward(x1, *Ws, n_heads=H), x1 @ Wv @ Wo)       # T=1
```
**Follow-ups:**
- *GQA / MQA:* use `n_kv_heads < n_heads`. Project K and V to `(B,T,Hkv,hd)`, then `np.repeat` each KV head `H/Hkv` times (or broadcast through a group axis). This shrinks the KV cache by a factor of H/Hkv, which is why Gemma and Llama use it.
- *Long T / memory:* FlashAttention-style tiling. Process K/V in blocks with an **online softmax**: keep a running max $m$ and denominator $\ell$, and when a new block raises the max, rescale with $e^{m_{old}-m_{new}}$. The memory then becomes O(T) instead of O(T²).
- *Padding mask:* OR a `(B,1,1,T)` key-padding mask into `mask`. Fully padded query rows are exactly why the NaN guard exists.
- *Incremental decoding:* see the KV cache in #5. Each step computes only the new query row against the cached K and V.

**Pattern hook:** "attention from scratch" → reshape/transpose heads, scale by √d_h, mask with −inf before a max-subtracted softmax.

## 5. Temperature + top-k + top-p (nucleus) sampling, and greedy decoding with a KV cache — Medium ✅ tested
**Prompt (as asked):** Given next-token logits `(V,)`, sample a token with temperature, optional top-k and optional top-p. Then explain how a greedy decode loop uses a KV cache.

**Clarify:** Order of operations? (Temperature → top-k → softmax → top-p, the same as HF.) Does T=0 mean greedy? (Yes.) Must top-p always keep ≥1 token? (Yes.) Batched? (Single row; batching is a follow-up.)

**Approach:**
- Temperature: $p_i \propto e^{z_i/T}$. T→0 approaches argmax, and T→∞ approaches uniform.
- Top-k: keep the logits that are ≥ the k-th largest. `np.partition` finds it in O(V) without a full sort.
- Top-p: sort the probabilities in descending order and keep the smallest prefix whose mass is ≥ p. Keep token $i$ if the cumulative mass *before* it is $< p$, which always keeps the top-1. Renormalize afterwards.
- Cost: O(V) for top-k, O(V log V) for top-p because of the sort.
```python
def sample_next(logits: np.ndarray, temperature: float = 1.0, top_k: Optional[int] = None,
                top_p: Optional[float] = None, rng: Optional[np.random.Generator] = None) -> int:
    """logits: (V,). Returns a token id."""
    rng = rng or np.random.default_rng()
    if temperature <= 0:
        return int(np.argmax(logits))                 # greedy
    z = logits.astype(np.float64) / temperature
    if top_k is not None and top_k < z.size:
        kth = np.partition(z, -top_k)[-top_k]         # O(V) k-th largest
        z = np.where(z < kth, -np.inf, z)
    p = np.exp(z - z.max()); p /= p.sum()
    if top_p is not None and top_p < 1.0:
        order = np.argsort(-p)
        cum = np.cumsum(p[order])
        keep = cum - p[order] < top_p                 # keep until mass >= top_p (always >=1 token)
        mask = np.zeros_like(p, dtype=bool); mask[order[keep]] = True
        p = np.where(mask, p, 0.0); p /= p.sum()
    return int(rng.choice(p.size, p=p))
```
**Greedy decoding with a KV cache (explain):**
1. **Prefill.** Run the whole prompt through the model once. For every layer, store `K, V` of shape `(B, Hkv, T_prompt, hd)` and take logits from the last position.
2. **Decode step.** Feed only the *new* token, which has length 1. Each layer computes its own q, k and v, **appends** k and v to the cache, and attends with $q_t$ against all cached $K_{\le t}, V_{\le t}$. No causal mask is needed because the cache contains only the past.
3. `next = argmax(logits)` (or `sample_next`). Stop at EOS or max_len.

Without the cache, each step recomputes all T positions, so a step costs O(T²·D) and a full generation costs O(T³·D). With the cache, a step costs O(T·D) for attention plus O(D²) for the MLP. Cache memory is $2 \cdot L \cdot H_{kv} \cdot d_h \cdot T \cdot$ bytes, per sequence. That memory is the real serving bottleneck, which motivates GQA/MQA and paged caches.

**Tests:**
```python
assert sample_next(logits, temperature=0) == 0                         # greedy
assert set(sample_next(logits, top_k=2, rng=rng) for _ in range(500)) == {0, 1}
assert all(sample_next(logits, top_p=1e-9, rng=rng) == 0 for _ in range(50))
assert set(sample_next(logits, top_p=0.8, rng=rng) for _ in range(1000)) == {0, 1}   # .61+.22
assert np.allclose(empirical_freqs_T1, softmax(logits), atol=0.015)     # 20k draws
assert sample_next(np.array([1e4, 0.0]), rng=rng) == 0                  # no overflow
```
**Follow-ups:**
- *Batched:* use `(B,V)` and `np.take_along_axis` over the per-row sorted indices. To sample, compare `cumsum` against `rng.random((B,1))`, which is inverse-CDF sampling.
- *How does vLLM batch this?* **Continuous batching.** The scheduler adds and removes sequences at every decode step instead of waiting for the whole batch to finish. **PagedAttention** stores the KV cache in fixed-size blocks through a per-sequence block table, like OS virtual memory. That removes fragmentation, enables prefix sharing (copy-on-write for beam search and parallel sampling), and lets prefill and decode mix in the same step.
- *Faster decoding:* speculative decoding. A small draft model proposes k tokens and the big model verifies them in one forward pass. Accept or reject so that the output distribution is exactly the target's.
- *Min-p / repetition penalty:* min-p keeps tokens with $p_i \ge \text{min\_p}\cdot p_{max}$. A repetition penalty divides positive logits (or multiplies negative ones) for tokens that have already been generated.

**Pattern hook:** "decode / generate" → temperature-scale, then truncate with top-k and top-p, renormalize, and sample. Mention prefill vs decode and the KV cache unprompted.

## 6. Byte-pair encoding: train merges + encode (pure Python) — Medium ✅ tested
**Prompt (as asked):** Given a small corpus, learn `num_merges` BPE merges by repeatedly merging the most frequent adjacent symbol pair. Then encode a new string with the learned merges.

**Clarify:** Pre-tokenize on whitespace? (Yes.) Use an end-of-word marker? (Yes, `</w>`, as in Sennrich et al.) How to break ties? (Deterministically: take the max `(count, pair)`.) Bytes or characters? (Characters here; byte-level BPE as in GPT-2 starts from the 256 bytes instead.)

**Approach:**
- **Train.** Represent the corpus as a `word-tuple → frequency` map. Each round:
  1. Count adjacent pairs, weighted by word frequency.
  2. Pick the argmax pair.
  3. Rewrite every word with that pair merged.

  The naive version costs O(M · N), where N is the total number of symbols across unique words.
- **Encode.** Merges must be applied **in the order they were learned**, which is not greedy longest-match. Give each merge a rank, and repeatedly merge the adjacent pair with the lowest rank until no pair is in the table. The naive loop is O(L²) per word, or O(L log L) with a heap and linked list.
```python
def _merge(sym: Tuple[str, ...], pair: Pair) -> Tuple[str, ...]:
    out, i = [], 0
    while i < len(sym):
        if i + 1 < len(sym) and (sym[i], sym[i + 1]) == pair:
            out.append(sym[i] + sym[i + 1]); i += 2
        else:
            out.append(sym[i]); i += 1
    return tuple(out)

def train_bpe(corpus: str, num_merges: int) -> List[Pair]:
    # word -> frequency; each word starts as a tuple of chars + end-of-word marker
    vocab: Dict[Tuple[str, ...], int] = Counter(
        tuple(w) + ('</w>',) for w in corpus.split())
    merges: List[Pair] = []
    for _ in range(num_merges):
        pairs: Counter = Counter()
        for sym, f in vocab.items():
            for a, b in zip(sym, sym[1:]):
                pairs[(a, b)] += f
        if not pairs:
            break
        best = max(pairs, key=lambda p: (pairs[p], p))   # tie-break deterministically
        merges.append(best)
        vocab = Counter({_merge(s, best): f for s, f in vocab.items()})
    return merges

def encode(text: str, merges: List[Pair]) -> List[str]:
    rank = {p: i for i, p in enumerate(merges)}
    out: List[str] = []
    for w in text.split():
        sym = tuple(w) + ('</w>',)
        while len(sym) > 1:
            cand = min(zip(sym, sym[1:]), key=lambda p: rank.get(p, float('inf')))
            if cand not in rank:
                break
            sym = _merge(sym, cand)                       # apply earliest-learned merge
        out.extend(sym)
    return out
```
**Dry run:** The corpus is `low×5, lower×2, newest×6, widest×3`. The pairs `e s`, `s t` and `t </w>` each have count 9, and the tie-break picks `t</w>`, then `st</w>`, then `est</w>`, then `ow`, then `low`. Encoding the unseen word `"lowest"` gives `["low", "est</w>"]`.

**Tests:**
```python
assert m[:3] == [('t', '</w>'), ('s', 't</w>'), ('e', 'st</w>')]
assert encode("newest", m) == ["newest</w>"]
assert encode("lowest", m) == ["low", "est</w>"]                # unseen word, learned pieces
assert encode("xyz", m) == ['x', 'y', 'z', '</w>']              # OOV -> characters
assert train_bpe("", 5) == [] and encode("", m) == []
assert train_bpe("a", 5) == [('a', '</w>')]                     # runs out of pairs early
```
**Follow-ups:**
- *Speed up training:* keep a pair→count map and a pair→words index, and update counts only for the words that contain the merged pair. Use a max-heap with lazy deletion. Training then runs in roughly O(N log N) total instead of O(M·N).
- *Byte-level BPE:* starting from 256 byte symbols means there are no unknown tokens. Pre-tokenize with a regex so merges never cross word or punctuation boundaries. SentencePiece (Gemini's tokenizer family) treats whitespace as `▁` and also supports unigram LM tokenization.
- *Decode:* concatenate the tokens and replace `</w>` with a space. This round-trips exactly, which is lossless by construction.

**Pattern hook:** "tokenizer from scratch" → count pairs weighted by word frequency, merge the argmax, and encode by lowest merge rank (not longest match).

## 7. AUC-ROC and nDCG@k from scratch (NumPy) — Medium ✅ tested
*(k-means was skipped, as allowed. It is already on a revision sheet: `coding_linkedin_l1l2knnkmeans`.)*

**Prompt (as asked):** (a) Given binary labels and scores, compute ROC AUC without sklearn. (b) Given graded relevances listed in the order the model ranked them, compute nDCG@k.

**Clarify:** How to handle tied scores in AUC? (Count each tie as ½.) What if there is only one class? (Undefined, so raise.) Which nDCG gain? (Exponential $2^{rel}-1$; linear is also common, so ask.) What if there are no relevant items? (nDCG = 0.)

**Approach:**
- **AUC.** Brute force compares every (pos, neg) pair, which is O(P·N). AUC equals the Mann-Whitney U statistic normalized: $\mathrm{AUC}=P(s^+>s^-)+\tfrac12P(s^+=s^-) = \frac{\sum_{i\in pos} R_i - \frac{n_+(n_++1)}{2}}{n_+ n_-}$, where $R_i$ are 1-based ranks in ascending score order, with the *average* rank assigned inside each tie group. This takes O(n log n). Equivalently, you can sweep thresholds and integrate the ROC curve with the trapezoid rule.
- **nDCG@k.** $\mathrm{DCG@k}=\sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}$ and $\mathrm{nDCG@k}=\mathrm{DCG@k}/\mathrm{IDCG@k}$, where IDCG uses the relevances sorted in descending order. This takes O(n log n).
```python
def auc_roc(y: Sequence[int], s: Sequence[float]) -> float:
    """P(score_pos > score_neg), ties count 1/2. Mann-Whitney U via average ranks."""
    y, s = np.asarray(y), np.asarray(s, dtype=float)
    n_pos, n_neg = int(y.sum()), int(len(y) - y.sum())
    if n_pos == 0 or n_neg == 0:
        raise ValueError("AUC undefined with one class")
    order = np.argsort(s, kind="mergesort")
    ss = s[order]
    ranks = np.empty(len(s))
    i = 0
    while i < len(ss):                                 # average rank over tie groups
        j = i
        while j + 1 < len(ss) and ss[j + 1] == ss[i]:
            j += 1
        ranks[order[i:j + 1]] = (i + j) / 2 + 1        # 1-based
        i = j + 1
    u = ranks[y == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))

def ndcg_at_k(rel_in_ranked_order: Sequence[float], k: int) -> float:
    r = np.asarray(rel_in_ranked_order, dtype=float)
    disc = 1.0 / np.log2(np.arange(2, k + 2))          # positions 1..k -> log2(i+1)
    dcg = ((2 ** r[:k] - 1) * disc[:len(r[:k])]).sum()
    ideal = np.sort(r)[::-1][:k]
    idcg = ((2 ** ideal - 1) * disc[:len(ideal)]).sum()
    return float(dcg / idcg) if idcg > 0 else 0.0
```
**Dry run (AUC):** y = `[0,0,1,1]`, s = `[.1,.4,.35,.8]`. Ascending ranks are .1→1, .35→2, .4→3, .8→4. The positives' rank sum is 2+4 = 6, so U = 6 − 3 = 3, and AUC = 3/4 = 0.75.

**Tests:** fuzzed against the O(P·N) pairwise brute force with heavy ties (300 cases).
```python
assert auc_roc([0, 0, 1, 1], [0.1, 0.4, 0.35, 0.8]) == 0.75
assert auc_roc([0, 1], [0.2, 0.9]) == 1.0 and auc_roc([1, 0], [0.2, 0.9]) == 0.0
assert auc_roc([0, 1, 0, 1], [0.5] * 4) == 0.5          # all ties
assert ndcg_at_k([3, 2, 1, 0], 4) == 1.0 and ndcg_at_k([0, 0, 0], 3) == 0.0
assert np.isclose(ndcg_at_k([1, 0], 5), 1.0) and ndcg_at_k([0, 1], 1) == 0.0
```
**Follow-ups:**
- *Streaming or too big for memory:* bucket the scores into a fixed histogram per class (for example 10k bins over [0,1]). AUC is then approximately $\sum_b \text{pos}_b \cdot(\text{neg below } b + \tfrac12 \text{neg}_b)/(n_+n_-)$, computed in one pass with O(bins) memory. This is how TF/Keras `AUC` works. It is distributed-friendly because the histograms just add.
- *PR-AUC vs ROC-AUC:* under heavy class imbalance (CTR, retrieval), ROC-AUC looks optimistic. Report PR-AUC (average precision) as well.
- *nDCG across queries:* average per query, and decide whether queries with IDCG = 0 are skipped or counted as 0. Must the ideal ranking use *all* judged docs, not just the retrieved ones? Yes. Otherwise the metric is inflated.
- *k-means (Lloyd's), in one line:* alternate `argmin` assignment (via $\|x\|^2 - 2x\cdot c + \|c\|^2$) and centroid means. Use k-means++ init, and re-seed empty clusters.

**Pattern hook:** "AUC from scratch" → rank-sum (Mann-Whitney) with average ranks for ties. "Ranking quality" → DCG with a log2 discount, normalized by the ideal ordering.
