# Tier 2 — Graph modelling, trees, linked lists

Four Tier 2 must-dos: LC 815 Bus Routes (BFS over routes), LC 297 Serialize and Deserialize Binary Tree (class design, preorder and BFS), LC 23 Merge k Sorted Lists (heap and divide and conquer), LC 148 Sort List (linked-list merge sort).
These test whether you can pick the right graph nodes, design a round-trippable format, and manipulate pointers without bugs.
All solutions were tested in scratch files with python3.

## 1. LC 815 — Bus Routes (BFS on a route graph) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** `routes[i]` is the list of stops bus i loops through forever. You start at stop `source` (not on a bus) and want to reach `target`. Return the minimum number of buses you must take, or -1.
`routes=[[1,2,7],[3,6,7]], source=1, target=6 -> 2` (bus 0 to stop 7, then bus 1). `routes=[[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15 -> 12 -> -1`.

**Clarify:** If source == target, is the answer 0? (Yes.) Are stops arbitrary ints up to 1e6? (Yes, so use a dict, not an array.) Are stops within a route distinct? (Assume yes.) Does the cost count buses, not stops? (Yes.)

**Approach:**
- **Brute force:** BFS over stops, with an edge between every pair of stops on the same route. A route with L stops adds O(L²) edges, so one 1e5-stop route blows up.
- **Key insight / modelling choice:** the cost is per bus, so make **routes the nodes**. Two routes are adjacent when they share a stop. BFS level = number of buses taken. The start frontier is every route containing `source` (level 1), and we stop as soon as we expand a route containing `target`. We never build route-route edges explicitly. Instead we go route → its stops → `stop_to_routes[stop]`, and mark each stop as seen so its route list is scanned only once.
- **Optimal:** S = Σ len(routes[i]). The index costs O(S), and each stop and route is expanded at most once, so BFS is **O(S) time, O(S) space**. Building explicit route-route edges would cost O(R²·L) instead.
```python
def num_buses_to_destination(routes: List[List[int]], source: int, target: int) -> int:
    # O(S) time, O(S) space, S = total stops across routes
    if source == target:
        return 0
    stop_to_routes: dict[int, list[int]] = defaultdict(list)
    for r, stops in enumerate(routes):
        for s in stops:
            stop_to_routes[s].append(r)
    q = deque()
    seen_route = [False] * len(routes)
    for r in stop_to_routes[source]:
        seen_route[r] = True
        q.append((r, 1))
    seen_stop = {source}
    while q:
        r, buses = q.popleft()
        for s in routes[r]:
            if s == target:
                return buses
            if s in seen_stop:
                continue
            seen_stop.add(s)
            for nr in stop_to_routes[s]:
                if not seen_route[nr]:
                    seen_route[nr] = True
                    q.append((nr, buses + 1))
    return -1
```
**Dry run:** `[[1,2,7],[3,6,7]], 1 -> 6`. stop_to_routes: 1→[0], 7→[0,1], 6→[1]. q=[(0,1)]. Pop route 0 and scan 1, 2, 7. Stop 7 enqueues (1,2). Pop route 1 and scan 3, 6. 6 == target, so return 2.

**Edge cases & tests:**
- source == target → 0, even if the stop isn't on any route.
- source isn't on any route → -1. Target unreachable → -1.
- A direct route works even when other routes also connect.
- A chain of routes gives the count of hops.
```python
assert num_buses_to_destination([[1,2,7],[3,6,7]], 1, 6) == 2
assert num_buses_to_destination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12) == -1
assert num_buses_to_destination([[1,2,3]], 5, 5) == 0
assert num_buses_to_destination([[1,2]], 9, 2) == -1
assert num_buses_to_destination([[1,2],[2,3],[3,4],[4,5]], 1, 5) == 4
assert num_buses_to_destination([[1,5],[1,2],[2,5]], 1, 5) == 1
```
**Follow-ups:**
- *Weighted (fare per bus / travel time)?* Run Dijkstra on the same route-node graph, or on a stop+route state graph if the time depends on the stop.
- *Many queries on a static network?* Precompute the route graph with BFS from each route, or use bidirectional BFS for each query.
- *Return the actual buses?* Store a parent route per route and walk back from the route that hit the target.

**Pattern hook:** if the cost counts *groups/lines/colors* rather than steps, make the groups the BFS nodes (a bipartite stop↔route graph, with BFS counting route layers).

## 2. LC 297 — Serialize and Deserialize Binary Tree (DFS preorder / BFS, class design) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** Design a `Codec` class with `serialize(root) -> str` and `deserialize(data) -> root` such that `deserialize(serialize(t))` equals `t` structurally. The format is up to you.
`[1,2,3,null,null,4,5]` → e.g. `"1,2,#,#,3,4,#,#,5,#,#"` → the same tree.

**Clarify:** Can values be negative or multi-digit? (Yes, so use a delimiter.) Are there duplicate values? (Yes, so you can't rebuild from inorder+preorder.) How should the empty tree be handled? (It must round-trip.) Is depth bounded? (Up to about 1e4 nodes, so recursion depth matters in Python.)

**Approach:**
- **Brute force idea:** preorder + inorder lists. This breaks with duplicates and needs two traversals.
- **Key insight:** one traversal is enough **if you record null children**. With `#` markers, preorder is unambiguous: each token is either a leaf-terminator or a node followed by exactly two subtrees. Deserialize by consuming tokens from a shared iterator in the same order.
- **Optimal:** O(n) time and O(n) space both ways. Recursion depth is O(h).
```python
class Codec:  # preorder + '#' markers; O(n) time/space, O(h) stack
    def serialize(self, root: Optional[TreeNode]) -> str:
        out: list[str] = []
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))
        def build() -> Optional[TreeNode]:
            tok = next(tokens)
            if tok == "#":
                return None
            node = TreeNode(int(tok))
            node.left = build()
            node.right = build()
            return node
        return build()
```
**BFS alternative** (the LeetCode format, iterative, so skewed trees can't hit the recursion limit). It runs in O(n):
```python
class CodecBFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        out, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                out.append(str(node.val)); q.append(node.left); q.append(node.right)
            else:
                out.append("#")
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "#":
            return None
        root = TreeNode(int(vals[0])); q, i = deque([root]), 1
        while q:
            node = q.popleft()
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i])); q.append(node.left)
            if vals[i + 1] != "#":
                node.right = TreeNode(int(vals[i + 1])); q.append(node.right)
            i += 2
        return root
```
**Dry run:** For tree 1(2, 3(4,5)), serialize gives `1,2,#,#,3,4,#,#,5,#,#`. In deserialize, build() reads 1. Its left build() reads 2, then # and # make 2 a leaf. Its right build() reads 3, which takes 4 (with #,#) and 5 (with #,#). The original tree is restored.

**Edge cases & tests:** The cases are the empty tree (`"#"`), a single node, left- and right-skewed trees, negatives, duplicates, and a 5000-deep chain (BFS version). Helpers:
```python
def build(level: list) -> Optional[TreeNode]:          # LeetCode list -> tree
    if not level or level[0] is None: return None
    root = TreeNode(level[0]); q, i = deque([root]), 1
    while q and i < len(level):
        node = q.popleft()
        if level[i] is not None: node.left = TreeNode(level[i]); q.append(node.left)
        i += 1
        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i]); q.append(node.right)
        i += 1
    return root

def same(a, b) -> bool:
    if not a or not b: return a is b
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

for codec in (Codec(), CodecBFS()):
    for c in [[1,2,3,None,None,4,5], [], [1], [-1,None,-2,None,-3], [5,5,5,None,5]]:
        assert same(codec.deserialize(codec.serialize(build(c))), build(c))
assert Codec().serialize(build([1,2,3,None,None,4,5])) == "1,2,#,#,3,4,#,#,5,#,#"
assert Codec().serialize(None) == "#"
assert not same(build([1,2]), build([1,None,2]))
```
**Follow-ups:**
- *Make it compact.* For a **BST**, preorder alone with no null markers is enough: rebuild with (lo, hi) bounds (LC 449). Otherwise, use binary encoding (varint values plus a bitmap of null children) and trim trailing `#`s in BFS.
- *Deep or huge trees?* Use BFS or an explicit-stack DFS to avoid recursion limits. To stream, write tokens to a file or socket as you go and deserialize from a token generator, since preorder needs only one pass and O(h) memory.
- *N-ary tree?* Write `val,childcount` per node in preorder (LC 428).

**Pattern hook:** "encode a structure as a string" means one traversal with explicit null or size markers, decoded by consuming tokens in the same order.

## 3. LC 23 — Merge k Sorted Lists (heap / divide and conquer) — Hard — Tier 2 ✅ tested
**Prompt (as asked):** Given an array of k sorted linked lists, merge them into one sorted linked list and return its head.
`[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]`; `[] -> []`; `[[]] -> []`.

**Clarify:** Can lists be empty or None? (Yes.) Can k be 0? (Yes.) Can we reuse the nodes rather than allocate? (Yes.) What are the sizes? (N total nodes up to about 1e4, k up to about 1e4.)

**Approach:**
- **Brute force:** dump all values, sort, and rebuild: O(N log N). Merging lists one at a time into an accumulator is O(kN).
- **Key insight:** the next output is always the min of the k current heads, so keep them in a **min-heap of size k**. Put `(val, list_idx, node)` in the heap, because the index breaks ties so Python never compares ListNodes.
- **Optimal:** heap merge is **O(N log k) time, O(k) space**. Divide and conquer (pairwise merging in log k rounds, where each round touches N nodes) is also **O(N log k)**, with **O(1) extra space** when done iteratively.
```python
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # heap: O(N log k) time, O(k) space
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

def merge_two(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val: tail.next, a = a, a.next
        else:              tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next

def merge_k_dc(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # divide & conquer: O(N log k) time, O(1) extra space
    if not lists:
        return None
    lists, step = list(lists), 1
    while step < len(lists):
        for i in range(0, len(lists) - step, 2 * step):
            lists[i] = merge_two(lists[i], lists[i + step])
        step *= 2
    return lists[0]
```
**Dry run (heap):** The heap starts as {(1,0),(1,1),(2,2)}. Pop (1,0) and push 4. Pop (1,1) and push 3. Pop 2 and push 6. Pop 3, then 4, 4, 5, 6. The output is 1,1,2,3,4,4,5,6.

**Edge cases & tests:** The cases are `[]`, `[None]`, a mix of None and non-empty lists, negatives, duplicates, and 200 random cases compared against `sorted()` for both versions.
```python
for f in (merge_k_lists, merge_k_dc):
    assert to_list(f([mk([1,4,5]), mk([1,3,4]), mk([2,6])])) == [1,1,2,3,4,4,5,6]
    assert to_list(f([])) == []
    assert to_list(f([None])) == []
    assert to_list(f([None, mk([1]), None])) == [1]
    assert to_list(f([mk([-3,-1]), mk([-2]), mk([0,0,0])])) == [-3,-2,-1,0,0,0]
```
**Follow-ups:**
- *Streaming inputs (iterators / infinite feeds)?* The heap version works as-is with iterators: keep `(val, idx)` plus each source's iterator and yield lazily (`heapq.merge`). Memory is O(k) regardless of N. Divide and conquer needs materialized lists, so the heap is the streaming answer.
- *k very large (can't hold k heads, e.g. 1e6 files)?* Use multi-pass external merge: merge in batches of B files (B = what fits in memory/file handles) into intermediate runs, then repeat. That takes log_B(k) passes, each reading N records sequentially. This is the classic external sort.
- *Distributed?* Have each shard merge locally, then do a tree-of-mergers (the divide and conquer shape) or a final k-way heap merge at a coordinator.

**Pattern hook:** for "merge / next-smallest across k sorted sources", keep a heap of k frontier elements, giving N log k.

## 4. LC 148 — Sort List (linked-list merge sort) — Medium — Tier 2 ✅ tested
**Prompt (as asked):** Sort a singly linked list in ascending order in O(n log n) time. Follow-up: use O(1) extra space.
`4->2->1->3 -> 1->2->3->4`; `-1->5->3->4->0 -> -1->0->3->4->5`.

**Clarify:** Can the list be empty? (Yes.) Duplicates? (Yes. Keep it stable.) Can we relink the nodes instead of swapping values? (Yes, relink.) Is copying to an array allowed? (No. That's the brute force.)

**Approach:**
- **Brute force:** copy the values to an array, sort, and write them back. That's O(n log n) but O(n) space, and dodges the point of the question.
- **Key insight:** merge sort fits linked lists. You split with slow/fast pointers and merge by relinking, with no random access or extra arrays. Start `fast = head.next` so that slow stops at the **end of the left half**, which guarantees that a 2-node list splits into 1+1 (otherwise it recurses forever).
- **Optimal (top-down):** **O(n log n) time, O(log n) recursion stack.**
- **Bottom-up for O(1) space:** count n, then for size = 1, 2, 4, … walk the list cutting off two runs of `size` nodes, merge them, and attach the result after a `prev` tail. This takes log n passes of O(n) with no recursion. Its helpers are `split(head, k)`, which cuts after k nodes and returns the rest, and `merge_into(prev, a, b)`, which returns the new tail. Both are tested.
```python
def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # top-down merge sort: O(n log n) time, O(log n) stack
    if not head or not head.next:
        return head
    slow, fast = head, head.next          # slow ends at end of left half
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid, slow.next = slow.next, None      # cut
    left, right = sort_list(head), sort_list(mid)
    dummy = tail = ListNode()
    while left and right:
        if left.val <= right.val:         # <= keeps it stable
            tail.next, left = left, left.next
        else:
            tail.next, right = right, right.next
        tail = tail.next
    tail.next = left or right
    return dummy.next
```
**Dry run:** For 4,2,1,3, slow stops at 2, giving the halves [4,2] and [1,3]. [4,2] splits into [4] and [2] and merges to [2,4]. [1,3] splits into [1] and [3] and merges to [1,3]. Merging [2,4] and [1,3] gives 1,2,3,4.

**Edge cases & tests:** The cases are empty, one node, two nodes in reverse order (the split-termination check), duplicates, negatives, and 300 random lists of length 0–40 checked against `sorted()`. Both the top-down and bottom-up versions are tested.
```python
for f in (sort_list, sort_list_bottom_up):
    assert to_list(f(mk([4,2,1,3]))) == [1,2,3,4]
    assert to_list(f(mk([-1,5,3,4,0]))) == [-1,0,3,4,5]
    assert to_list(f(mk([]))) == []
    assert to_list(f(mk([7]))) == [7]
    assert to_list(f(mk([2,1]))) == [1,2]
    assert to_list(f(mk([3,3,1,1]))) == [1,1,3,3]
```
**Follow-ups:**
- *Why not quicksort?* It's O(n²) worst case, and partitioning a list is fiddly. Merge sort is stable with a guaranteed n log n.
- *Doubly linked list or too big for memory?* For a list that doesn't fit, use external merge sort: sort chunks in memory, write the runs out, then k-way merge them (see #3).
- *Nearly sorted input?* Use natural merge sort: detect the existing ascending runs and merge only those, which is O(n) for already-sorted input.

**Pattern hook:** for "sort a linked list" or "O(n log n) without random access", use merge sort with slow/fast split and dummy-head merge. For O(1) space, merge bottom-up.
