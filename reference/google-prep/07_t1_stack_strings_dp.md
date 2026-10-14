# Tier 1 — Monotonic stack, strings, 2D string DP

Four Tier 1 must-dos: **LC 84** Largest Rectangle in Histogram (+85), **LC 5** Longest Palindromic Substring, **LC 68** Text Justification, and **LC 10** Regular Expression Matching (+44).
Every solution was tested in a scratch file with fixed asserts plus randomized checks against a brute-force or library oracle (`re.fullmatch`, `fnmatch`).

## 1. LC 84 — Largest Rectangle in Histogram (monotonic stack) — Hard — Tier 1 ✅ tested
**Prompt (as asked):** Given bar heights (width 1 each), return the area of the largest rectangle in the histogram.
Example: `[2,1,5,6,2,3]` → `10` (bars 5,6 × width 2). Example: `[2,4]` → `4`.

**Clarify:** Can it be empty? (yes → 0). Are there zeros? (yes, they split the histogram). Are heights non-negative ints? (yes). Is n up to 1e5? (yes → need O(n)).

**Approach:** Brute force: for every i, extend j while tracking the min height, O(n²). Key insight: every bar's best rectangle is bounded by the first smaller bar on each side. Keep a stack of indices with **increasing** heights. When bar `h` is ≤ the top, pop it. The popped bar's right boundary is `i` and its left boundary is the new top (or -1), so width = `i - left - 1`. A sentinel `0` appended at the end flushes the stack, so there's no post-loop cleanup. Each index is pushed and popped once: **O(n) time, O(n) space.**
```python
def largestRectangleArea(heights: List[int]) -> int:  # O(n) time, O(n) space
    stack: List[int] = []  # indices, heights strictly increasing
    best = 0
    for i, h in enumerate(heights + [0]):  # sentinel 0 flushes the stack
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, height * (i - left - 1))
        stack.append(i)
    return best
```
**Dry run:** `[2,1,5,6,2,3]`. At i=1 (h=1), pop 2 → 2×1. Push 1, 5, 6. At i=4 (h=2), pop 6 → 6×1 = 6, then pop 5 → 5×(4−1−1) = 10. Push 2, 3. At the sentinel, pop 3 → 3, pop 2 → 2×4 = 8, pop 1 → 1×6 = 6. Answer **10**.

**Edge cases & tests:**
- Empty input, a single bar, all-equal bars (the `>=` pop still yields the correct full width at the last pop), strictly increasing input, all zeros.
- `assert largestRectangleArea([2,1,5,6,2,3]) == 10`, `([2,4]) == 4`, `([]) == 0`, `([5]) == 5`, `([3,3,3]) == 9`, `([1,2,3,4,5]) == 9`, `([0,0]) == 0`, plus 500 random cases against the O(n²) brute force.

**Follow-ups:**
- *Streaming bars?* The stack works online. Bars still on the stack are "open", so the current best is a lower bound until you flush with the sentinel.
- *Divide and conquer?* Split at the min bar: O(n log n) on average, O(n²) worst case. A segment tree for the range-min gets it to O(n log n) worst case. The stack is simpler.
- *Trapping Rain Water (LC 42)?* It uses the same monotonic-stack skeleton with a decreasing stack.

**Pattern hook:** "For each element, find the nearest smaller (or larger) element on the left and right" → monotonic stack. Popping happens at the moment you discover the right boundary.

**Sibling: LC 85 Maximal Rectangle.** Treat each row of the binary matrix as the base of a histogram: `hist[j]` = the number of consecutive 1s ending at this row in column j (it resets to 0 on a '0'). Run LC 84 on every row's histogram. **O(R·C) time, O(C) space.**
```python
def maximalRectangle(matrix: List[List[str]]) -> int:  # O(R*C)
    if not matrix: return 0
    hist = [0] * len(matrix[0]); best = 0
    for row in matrix:
        for j, c in enumerate(row):
            hist[j] = hist[j] + 1 if c == "1" else 0
        best = max(best, largestRectangleArea(hist))
    return best
```
Tests: the LC example → 6, `[["0"]]` → 0, `[["1"]]` → 1, `[]` → 0, a 2×2 matrix of all 1s → 4.

## 2. LC 5 — Longest Palindromic Substring (expand around center) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Return the longest substring of `s` that is a palindrome.
Example: `"babad"` → `"bab"` (or `"aba"`). Example: `"cbbd"` → `"bb"`.

**Clarify:** If several have the same length, can I return any of them? (yes). Is it case-sensitive, and only ASCII? (yes). Is n ≤ 1000? (yes, so O(n²) is fine). Empty string → `""`.

**Approach:** Brute force: check all O(n²) substrings, O(n) each → O(n³). 2D DP: `pal[i][j] = s[i]==s[j] and pal[i+1][j-1]` → O(n²) time and O(n²) space. Key insight: every palindrome mirrors around a center, and there are 2n−1 centers (n chars plus n−1 gaps). Expand outward from each center while the ends match. **O(n²) time, O(1) space.**
```python
def longestPalindrome(s: str) -> str:  # O(n^2) time, O(1) space
    if not s: return ""
    def expand(l: int, r: int) -> tuple:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return l + 1, r  # s[l+1:r] is the palindrome
    best = (0, 1)
    for c in range(len(s)):
        for l, r in (expand(c, c), expand(c, c + 1)):  # odd, even
            if r - l > best[1] - best[0]:
                best = (l, r)
    return s[best[0]:best[1]]
```
**Dry run:** `"cbbd"`. At c=0 the odd center gives "c". At c=1 the odd center gives "b", and the even center (1,2) matches b==b, then expands to (0,3) where c≠d and stops → span (1,3) = "bb". Nothing longer appears → **"bb"**.

**Edge cases & tests:**
- An empty string, a single char, two different chars, all the same char (the even center matters), and a long even palindrome in the middle.
- `assert longestPalindrome("cbbd") == "bb"`, `("babad") in ("bab","aba")`, `("a") == "a"`, `("") == ""`, `("aaaa") == "aaaa"`, `("forgeeksskeegfor") == "geeksskeeg"`, plus 300 random strings over {a,b} checked against a brute force (length, palindrome, and substring).

**Follow-ups:**
- *Manacher's algorithm (O(n)):* Insert separators (`#a#b#`) so every palindrome has odd length. Keep the rightmost palindrome found so far, with center `C` and right edge `R`. For a new center `i < R`, initialize its radius from the mirror `2C−i`, capped at `R−i`, and then expand only past `R`. `R` only ever moves right, so the total work is linear. Name it, state the O(n) bound, and say you'd write expand-around-center unless asked.
- *Count all palindromic substrings (LC 647)?* Use the same loop and add `(r-l+1)//2` per center, or just count each successful expansion.
- *Longest palindromic **subsequence** (LC 516)?* That's different: an interval DP `dp[i][j]`, O(n²).

**Pattern hook:** "Palindromic substring" plus n ≤ ~10⁴ → expand from 2n−1 centers. Use DP only when you need every `pal[i][j]` (for example, palindrome partitioning).

## 3. LC 68 — Text Justification (greedy string simulation) — Hard — Tier 1 ✅ tested
**Prompt (as asked):** Given words and `maxWidth`, pack as many words as fit per line (greedy). Fully justify each line by spreading spaces as evenly as possible, giving the extra spaces to the left gaps. The **last line**, and any line with a **single word**, is left-justified and padded with spaces on the right.
Example: `["This","is","an","example","of","text","justification."]`, 16 → `["This    is    an","example  of text","justification.  "]`.

**Clarify:** Is every word ≤ maxWidth? (yes). Can words be empty, or contain spaces? (no). Is the output exactly `maxWidth` per line, including trailing pad? (yes). Do the extras go to the leftmost gaps? (yes).

**Approach:** There's no clever algorithm here; it's careful simulation. (1) Greedily take words `i..j−1` while `letters + len(next) + gaps_so_far ≤ maxWidth`. (2) If the line is the last one or holds a single word, join with single spaces and right-pad. (3) Otherwise `q, r = divmod(maxWidth − letters, gaps)`: every gap gets `q` spaces, and the first `r` gaps get one more. **O(total chars) time**, output-sized space.
```python
def fullJustify(words: List[str], maxWidth: int) -> List[str]:  # O(L)
    res: List[str] = []
    i, n = 0, len(words)
    while i < n:
        j, length = i, 0  # greedily pack words[i:j]
        while j < n and length + len(words[j]) + (j - i) <= maxWidth:
            length += len(words[j]); j += 1
        gaps = j - i - 1
        if j == n or gaps == 0:  # last line or single word: left-justify
            line = " ".join(words[i:j])
            res.append(line + " " * (maxWidth - len(line)))
        else:
            q, r = divmod(maxWidth - length, gaps)
            line = ""
            for k in range(i, j - 1):
                line += words[k] + " " * (q + (1 if k - i < r else 0))
            res.append(line + words[j - 1])
        i = j
    return res
```
**Dry run:** For width 16, line 1: This(4)+is(2)+an(2) = 8 letters with 2 gaps → 10 ≤ 16. Adding "example" gives 8+7+3 = 18 > 16, so stop. Spaces = 8 over 2 gaps → q=4, r=0 → `"This    is    an"`. Line 2: example+of+text = 13 letters, 3 spaces over 2 gaps → q=1, r=1 → `"example  of text"`. Line 3 is the last line → `"justification.  "`.

**Edge cases & tests:**
- A single-word middle line (`"acknowledgment  "`), a last line with several words (single spaces only), one word exactly equal to the width, width 1, and a line that fits exactly.
- The three LC examples assert equal, plus `(["a"],1)==["a"]`, `(["abc"],5)==["abc  "]`, `(["a","b","c"],1)==["a","b","c"]`, `(["ab","c","d","efgh"],6)==["ab c d","efgh  "]`.

**Follow-ups:**
- *A word longer than maxWidth?* Clarify the rule: hard-break it with a hyphen, or let it overflow. In the packing loop, a line must always take at least one word, or you loop forever.
- *Minimize raggedness (pretty-printing, Knuth–Plass)?* That's a DP over break points: `dp[i] = min_j dp[j] + (slack(i..j))²`, O(n²). Greedy isn't optimal for that cost.
- *Streaming words?* Buffer only the current line and emit it when the next word doesn't fit. You can't justify the last line until the stream ends, so you need lookahead of one line.

**Pattern hook:** "Format text to width" → greedy pack, then `divmod` the spaces. Enumerate the special lines (last line, single word) before you code.

## 4. LC 10 — Regular Expression Matching (2D DP, bottom-up) — Hard — Tier 1 ✅ tested
**Prompt (as asked):** Implement full-string matching where `.` matches any single char and `x*` matches zero or more of the preceding element `x`.
Examples: `("aa","a")` → False. `("aa","a*")` → True. `("aab","c*a*b")` → True. `("mississippi","mis*is*p*.")` → False.

**Clarify:** Must the whole string match, not a substring? (yes). Is `*` always preceded by a valid char? (yes). Lowercase letters only? (yes). Can either string be empty? (yes, e.g. `("", "a*b*")` → True).

**Approach:** Brute force: recursion that branches on each `*`, exponential in the worst case. Key insight: the state is just the pair (position in s, position in p). Define `dp[i][j]` = "does `s[i:]` match `p[j:]`?", with base case `dp[m][n] = True`. Let `first = i<m and p[j] in {s[i], '.'}`.
- If `p[j+1] == '*'`, there are two choices:
  - **zero uses:** skip `x*` → `dp[i][j+2]`.
  - **one or more uses:** `first and dp[i+1][j]`. This consumes one char of s and **stays** on `x*` so it can consume again.
- Otherwise, `dp[i][j] = first and dp[i+1][j+1]`.

Fill i from m down to 0 (**including i = m**, because `x*` can match the empty suffix) and j from n−1 down to 0. **O(m·n) time and space.** Space drops to O(n) with two rows.
```python
def isMatch(s: str, p: str) -> bool:  # O(m*n) time, O(m*n) space
    m, n = len(s), len(p)
    # dp[i][j]: s[i:] matches p[j:]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[m][n] = True
    for i in range(m, -1, -1):
        for j in range(n - 1, -1, -1):
            first = i < m and p[j] in (s[i], ".")
            if j + 1 < n and p[j + 1] == "*":
                # skip "x*" entirely, OR consume one char and stay on "x*"
                dp[i][j] = dp[i][j + 2] or (first and dp[i + 1][j])
            else:
                dp[i][j] = first and dp[i + 1][j + 1]
    return dp[0][0]
```
**Dry run:** `("aab","c*a*b")`. With i=3 (empty suffix): `dp[3][4]` ('b') = F, `dp[3][2]` ('a*') = skip → `dp[3][4]` = F, `dp[3][0]` = F. With i=2 ('b'): `dp[2][4]` = b==b and `dp[3][5]` = T, then `dp[2][2]` = skip → T. With i=1 and i=0 ('a'): `dp[i][2]` = first and `dp[i+1][2]` = T. Then `dp[0][0]` ('c*') = skip → `dp[0][2]` = **T**.

**Edge cases & tests:**
- Both strings empty, an empty s with a pattern of all `x*`, an empty s with `"a"`, `.*` matching anything, and a `*` that has to match zero times.
- `assert not isMatch("aa","a")`, `isMatch("aa","a*")`, `isMatch("ab",".*")`, `isMatch("aab","c*a*b")`, `not isMatch("mississippi","mis*is*p*.")`, `isMatch("","a*b*")`, `not isMatch("","a")`, `isMatch("","")`, plus 2000 random (s, p) pairs checked against `re.fullmatch`.

**Follow-ups:**
- *Top-down instead?* Use `@lru_cache` on `(i, j)` with the same transitions. It's often faster to write, and it visits only reachable states.
- *Add `+` or `?`?* Rewrite them first: `x+` = `xx*`, and `x?` = "skip, or match one and advance j by 2".
- *A huge text with a fixed pattern?* Compile the pattern to an NFA (Thompson). Simulating the set of active states is O(|s|·|p|) time but O(|p|) memory and streams over s. Converting to a DFA gives O(|s|) at the cost of a possible state blow-up.

**Pattern hook:** "Does string A match pattern/string B" → 2D DP on suffixes (i, j). For each special char, write out the "use zero" and "use one more and stay" transitions.

**Sibling: LC 44 Wildcard Matching.** `?` matches exactly one char, and `*` matches any sequence on its own (it doesn't depend on the preceding char). Same suffix DP: `*` → `dp[i][j+1]` (match empty) **or** `dp[i+1][j]` (eat one char and stay on `*`). Otherwise the chars must match and you advance both. **O(m·n).** (Greedy two-pointer backtracking to the last `*` also works: O(m·n) worst case, O(1) space.)
```python
def isWildMatch(s: str, p: str) -> bool:  # O(m*n)
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[m][n] = True
    for i in range(m, -1, -1):
        for j in range(n - 1, -1, -1):
            if p[j] == "*":  # match empty OR eat one char of s and stay
                dp[i][j] = dp[i][j + 1] or (i < m and dp[i + 1][j])
            else:
                dp[i][j] = i < m and p[j] in (s[i], "?") and dp[i + 1][j + 1]
    return dp[0][0]
```
Tests: `("aa","a")` → F, `("aa","*")` → T, `("cb","?a")` → F, `("adceb","*a*b")` → T, `("acdcb","a*c?b")` → F, `("","***")` → T, `("","?")` → F, plus 2000 random pairs checked against `fnmatch.fnmatchcase`.
