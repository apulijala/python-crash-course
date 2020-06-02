# First attempt 15 minutes.
# Scored only 50%
import math

def find_missing_element(A):
    if len(A) == 0:
        return 1
    A.sort()
    i = 0
    while i < len(A):
        j = i + 1
        if j != A[i]:
            return j
        i = i + 1


"""
40 min
100%


"""
def min_difference(A):
    
    first_part_sum = A[0]
    second_part_sum = 0
    i = 1
    while i < len(A):
        second_part_sum += A[i]
        i = i + 1

    differences = []
    diff = second_part_sum - first_part_sum
    if diff < 0:
        diff = -1 * diff

    differences.append(diff)
    i = 1 # Start from the first element. 
    while i < len(A) -1:
        second_part_sum -= A[i]
        first_part_sum += A[i]
        diff = second_part_sum - first_part_sum
        # print(first_part_sum, second_part_sum, diff)
        if diff < 0:
            diff = -1 * diff
        i = i + 1

        differences.append(diff)
    # print(min(differences))
    return min(differences)
    
def frog_river_one(X, A):
    
    Y = X + 1
    found = {}
    for i in range(1,Y):
        try:
            found[i] = A.index(i)
        except ValueError:
            return -1
    return max(found.values())
                      


