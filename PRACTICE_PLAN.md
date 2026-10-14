# Practice Plan

## Core rule

Mix problem families every day. Do not spend a week or month on one topic.

Focus on:

- **Medium:** fast, clean implementation with correct edge cases.
- **Medium-hard:** unfamiliar modeling, a non-obvious invariant, or a strong follow-up.
- **Hard:** transferable problems with useful ideas, not obscure tricks.

Do not schedule Easy problems. If a basic operation is weak, review the implementation directly and use it inside a Medium problem.

## Daily mix

Use a 90–120 minute block:

1. **Spaced re-solve, 20–25 minutes:** one previous miss.
2. **New problem, 40–50 minutes:** Medium, Medium-hard, or Hard.
3. **Different pattern, 25–35 minutes:** a second problem, follow-up, or partial solve. It must not use the same main pattern as step 2.
4. **Review, 5–10 minutes:** record the miss, invariant, complexity, and next review date.

If there is only 60–75 minutes, do steps 1, 2, and 4. Do not replace the re-solve with another new problem.

### Selection rule

Choose each day's work from at least two different families:

- arrays, strings, hashing, two pointers, sliding windows
- trees, graphs, grids, topological sort, union-find
- intervals, heaps, sweep line, binary search
- dynamic programming, backtracking, greedy
- stacks, parsing, tries, linked lists
- data-structure design, streaming, randomization

Do not repeat the same primary family on consecutive days unless it is a scheduled re-solve. Tags stay hidden until after the attempt.

## Weekly target

- 6–8 new Medium or Medium-hard problems.
- 2–3 new Hard problems.
- 5–7 spaced re-solves from different families.
- 2 timed mixed sets with no shared primary pattern.
- 1 full mock or recorded verbal walkthrough.
- 1 review of repeated mistakes.
- Touch at least five of the six families above.

## Session format

For every new problem:

1. Restate the problem and clarify edge cases.
2. Give the brute-force approach and complexity.
3. Derive the better approach without looking at tags.
4. Code and test aloud.
5. Handle one follow-up: tighter complexity, larger input, streaming data, or an API change.
6. Record the pattern only after the attempt.

Stop reading solutions passively. If stuck, take one hint, close it, and finish the implementation yourself.

## Four-to-six-month progression

The problem mix stays broad in every month. Only the pressure changes.

### Months 1–2: accuracy and pattern recognition

- Use the full daily mix from day one.
- Bias selection toward high-value Google problems and current weaknesses.
- Time-box Mediums at 45 minutes and Hards at 60 minutes.
- Build the re-solve queue aggressively.

### Months 3–4: speed and follow-ups

- Keep the same mixed distribution.
- Increase timed sets and unfamiliar formulations.
- Require a clean explanation, test plan, and follow-up for every problem.
- Re-solve misses more often than solved-first-try problems.

### Months 5–6: interview simulation and repair

- Run two or three full coding mocks each week.
- Fill the remaining days with mixed problems chosen from the error log.
- Keep Hard problems transferable: graph modeling, DP state design, intervals, data structures, and proof-heavy greedy.
- Drop near-duplicates that do not expose a new decision or failure mode.

## Review schedule

- First miss or hint: re-solve after 2 days, 1 week, and 1 month.
- Slow but correct: re-solve after 1 week and 1 month.
- Clean first attempt: revisit only through a harder variant or follow-up.
- Repeated miss: stop adding new problems in that pattern until one re-solve is clean.

## Weekly check

At the end of each week, check:

- Did every day mix at least two problem families?
- Was the new-problem set limited to Medium, Medium-hard, and Hard?
- Which mistake appeared more than once?
- Which problem still cannot be explained without code?
- What should enter next week's re-solve queue?
