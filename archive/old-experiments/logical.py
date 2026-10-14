import heapq

def findCelebrity(n):

    candidate = 0
    for i in range(1,n):
        if knows(candidate, i):
            candidate = i
        
    for i in range(n):
        if candidate != i:
            if knows(candidate, i) or not knows(i, candidate):
                return -1
    return candidate


def kClosest(points, k):

    dist = lambda x: x[0]**2 + x[1]**2

    return heapq.nsmallest(k, points, key=dist)