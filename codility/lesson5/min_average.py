def min_average_of_slices(A):
    n = len(A)
    minimum = 20000
    min_index = -1
    P = prefix_sums(A)
    print(P)

    for i in range(0,n):
        for j in range(i+1, n ):
            total = count_total(P, i, j)
            avg = total/((j -i) + 1)
            if avg < minimum:
                minimum = avg
                min_index = i
    

    return min_index

"""
Slice includes first leemnt, but not the last one.
print(A[0:2]) will select 0 and 1
"""

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n+1):
        P[k] = A[k-1] + P[k-1]
    return P

"""
In this case is slice is x, y x and y are inclusive
Start at 12:52 - 15:00
"""

def count_total(P, x, y):
    return P[y + 1] - P[x]


