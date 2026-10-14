import random

def reservoir_sampling(stream, k):
    if k<=0:
        return []
    
    reservoir = []

    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0,i)

            if j < k:
                reservoir[j] = item
    
    return reservoir


        
def random_node(head):
    result = None
    node = head
    i = 1

    while node:
        if random.randint(1,i) == 1:
            result = node.val
        
        node = node.next
        i+=1
    return result

    

def fisher_yates(arr):
    for i in range(len(arr) - 1,0,-1):
        j = random.randint(0,i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def matmul(A,B):
    m = len(A)
    k = len(A[0])
    n = len(B[0])

    if k != len(B):
        raise ValueError

    C = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for t in range(k):
                C[i][j] += A[i][t] * B[t][j]
    return C