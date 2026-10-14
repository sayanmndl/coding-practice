# Coding Practice

My long-term coding interview practice repo. The target is Google-level problem solving over the next four to six months, not short-term memorization.

## Where to work

- `practice/`: new timed attempts, rewrites, and review notes.
- `solutions/google/`: Google-focused solutions imported from my current practice folder.
- `solutions/general/`: standalone algorithm problems.
- `solutions/non-ml/`: other software and algorithm exercises.
- `solutions/legacy/`: older linked-list, tree, and graph work already in this repo.
- `ml/`: ML algorithms implemented from scratch.
- `reference/google-prep/`: pattern notes, study plans, frequency data, coding cards, and the offline card viewer.
- `notes/`: problem lists and planning notes.
- `notebooks/`: scratch notebooks with saved outputs removed.
- `archive/old-experiments/`: older experiments kept for reference, not active practice.

## Practice loop

For each problem:

1. Restate the problem and clarify edge cases.
2. Give the brute-force approach and its complexity.
3. Identify the pattern and derive the better approach.
4. Code without copying an old answer.
5. Test normal cases, boundaries, and failure cases.
6. Record the result in `PROGRESS.md`.
7. Re-solve misses after 2 days, 1 week, and 1 month.

Use `practice/README.md` for file naming and the solution template.

## Four-to-six-month plan

Practice stays mixed from day one. Every day should combine at least two problem families, and every week should touch most of the major families. Do not reserve graphs, DP, trees, or other patterns for separate months.

Focus on Medium, Medium-hard, and transferable Hard problems. Do not schedule Easy problems.

- Months 1–2: improve accuracy and pattern recognition under a time limit.
- Months 3–4: add more timed mixed sets, unfamiliar wording, and follow-ups.
- Months 5–6: run frequent mocks and choose the remaining work from the error log.

Default week: 6–8 new Medium or Medium-hard problems, 2–3 new Hards, 5–7 mixed re-solves, two timed mixed sets, one mock or recorded walkthrough, and one rest day.

See `PRACTICE_PLAN.md` for the daily selection rule and review schedule.

Use [`notes/MASTER_1500.md`](notes/MASTER_1500.md) as the ranked mixed backlog. The filterable CSV and ranking method are in the same folder.

## Imported material

The first organized import combines the existing repository, the `googleprep/coding` collection, and the local `tests` practice folder. Virtual environments, caches, compiled binaries, logs, editor chat history, nested Git metadata, and notebook outputs were left out. They are generated or private artifacts, not practice material.
