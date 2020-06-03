def is_triangular(A):
    n = len(A)
    if n < 3:
        return 0
    
    A.sort()
    i = 0
    while i <= n-3:
        P = i
        Q = i + 1
        R = i + 2
        if (A[P] + A[Q] > A[R]) and (A[Q] + A[R] > A[P]) and (A[R] + A[P] > A[Q]):
            return 1
        i = i + 1

    return 0