def passing_cars(A):

    A = [0, 1, 0, 1, 1]
    num_passing = 0
    n = len(A)
    for i in range(0,n):
        if A[i] != 1:
            for j in range(i +1, n):
                if A[j] == 1:
                    num_passing = num_passing + 1
                    if num_passing > 1_000_000_000:
                        return -1

    return num_passing


def passing_cars_effecient(A):
    count_zeros = 0
    num_passing = 0
    i = 0
    n = len(A)
    while i < n:
        if A[i] == 0:
            count_zeros += 1
        else: # Assume 1 as it is only possiblity.
            num_passing += count_zeros
            if num_passing > 1_000_000_000:
                return -1 
            
        i = i + 1
    return num_passing


        
