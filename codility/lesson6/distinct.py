# 10: 15

def count_distinct(A):
    
    if len(A) == 0:
        return 0
    A.sort()
    i = 0
    n = len(A) - 1
    count = 1
    while i < n:
        if A[i] != A[i + 1]:
            count = count + 1
        i = i + 1
    
    return count