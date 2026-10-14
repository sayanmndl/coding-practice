# Writer spec — coding practice write-ups

## Context
- **Candidate:** Senior SWE/ML at Google ({{TEAM}}). The coding / DS&A round is 45 minutes, in person, Oct 13 2026, on a provided Chromebook (shared doc or interview.google.com, so there's likely no autocomplete or execution). Language: Python.
- **Their revision cards** (see `coding/google_coding_index.md`) are heavy on graph (26), intervals (14), design (11), heap/trie/unionfind, and light on **DP (6), binary search (1), sliding window (1), backtracking (2)**. Focus on the light areas, and don't duplicate problems already in the index (grep it).
- **Google style:** medium-to-hard, often a twist on a classic. Interviewers value clarifying questions, a stated brute force, then an optimization, clean code, self-testing with edge cases, complexity, and handling follow-ups such as "what if the input streams?" or "what if it doesn't fit in memory?".

## Per-problem format
```
## N. <Problem name> (<pattern>) — <difficulty>
**Prompt (as asked):** a 2–4 line statement, plus 1–2 examples.
**Clarify:** 3–4 questions with assumed answers.
**Approach:** brute force (complexity) → key insight → optimal (complexity). Include a recurrence/invariant where relevant.
```python
<clean, interview-quality solution with type hints, ≤40 lines>
```
**Dry run:** a short trace on the example.
**Edge cases & tests:** a bullet list, plus the asserts you'd say out loud.
**Follow-ups:** 2–3 likely follow-ups with answers (variants, streaming, memory, scale).
**Pattern hook:** one line on how to recognize this pattern next time.
```

## Mandatory verification
For EVERY solution, write it plus 5+ asserts (including edge cases) to a scratch file under `/private/tmp/claude-501/-Users-sayanmandal-workspaces-googleprep/2aa7106d-41e4-4890-ac08-201a44dee449/scratchpad/coding_<yourname>/` and run it with `python3`. Fix it until all pass. Only then paste the code into the markdown. Mention "✅ tested" in the problem header line.

## Process
Write the markdown file incrementally: create it with a header, then append one problem at a time with Bash heredocs. Touch only your own files.

## Must-do round (added Oct 8) — extra rules
- Each agent writes ONE file, named exactly as given in its prompt, titled `# <file title>`. Open the file with a 2–3 line intro listing the problems and their tier.
- Per-problem header format: `## N. LC <number> — <Name> (<pattern>) — <difficulty> — Tier <1|2> ✅ tested`. Number problems within the file starting at 1.
- Sibling problems named in the prompt (e.g. "+974") go in a **"Sibling:"** subsection after Follow-ups: a 3–5 line approach plus a ≤15-line tested solution.
- **Anti-stall rule (IMPORTANT):**
  1. Test ALL your solutions first, in scratch files.
  2. Then write the markdown with exactly ONE problem per Bash heredoc append, ≤500 words per call.
  3. Don't plan or think at length between appends; just write the next one.
- Python only. Tag each solution with its complexity.
