# Naming spec for coding revision cards

Rename each PNG to `<topic>_<technique>_<title>.png`. Examples: `graph_dfs_numberofislands.png`, `dp_knapsack_coinchange.png`, `slidingwindow_variable_longestsubstringnorepeat.png`.

- All lowercase. Within a segment, join words with no separator. Separate segments with `_`.
- **`<topic>`**: use ONLY this fixed vocabulary, so files sort together across agents:
  array, string, hashing, twopointers, slidingwindow, prefixsum, stack, monostack, queue, linkedlist, tree, bst, trie, heap, graph, unionfind, intervals, binarysearch, sorting, greedy, dp, backtracking, recursion, bitmanip, math, matrix, design, concurrency, simulation, mlcoding, patterns
  (`patterns` = multi-topic overview/cheatsheet cards; `mlcoding` = ML-flavoured coding like attention, k-means, sampling)
- **`<technique>`**: the main technique or subtopic, e.g. dfs, bfs, topo, dijkstra, unionfind, memo, tabulation, knapsack, lis, interval, twoheaps, kway, monotonic, fastslow, reverse, lca, traversal, serialize, sweepline, bisect, bitmask, cheatsheet, overview
- **`<title>`**: the problem name or card title, compacted (e.g. `numberofislands`, `lrucache`, `medianofdatastream`). Use the LeetCode-style problem name if the card shows one.
- If a card covers several problems, use the dominant one or a short summary (e.g. `graph_bfs_shortestpathfamily`).
- Never overwrite an existing file; check first. On a collision, append `_v2`, `_v3`.
- Leave the `_thumbnails/` folder untouched.
