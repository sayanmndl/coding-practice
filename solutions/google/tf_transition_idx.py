


def find_transition(arr):
    l = 0
    r = len(arr)-1

    while r - l > 1:
        m = (l+r)//2

        if arr[m]:
            l = m
        else:
            r = m
    return l