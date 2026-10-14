from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):

    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(numCourses) if in_degree == 0])

    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for neigh in graph[course]:
            in_degree[neigh] -= 1
            if in_degree[neigh] == 0:
                queue.append(neigh)

    return order if len(order) == numCourses else []