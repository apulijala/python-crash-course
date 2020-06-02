def passing_cars(A):
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

        
