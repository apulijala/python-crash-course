def count_elements(A, m):
    my_range = m + 1
    count = [0] * (my_range)
    print(A)
    print(count)
    print(list(range(1,5)))
    for i in A:
        count[i] += 1
    print(count)

def frog_jump(X, A):
    posistions_seconds = {}
    j = 0
    for i in A:
        if i not in posistions_seconds.keys():
            posistions_seconds[i] = j
        j = j + 1
    # print(posistions_seconds)
    Y = X + 1
    max = 0
    for i in range(1,Y):
        if i not in posistions_seconds.keys():
            return -1
        else: 
            if posistions_seconds[i] > max:
                max = posistions_seconds[i]

    return max

"""
N is the number of elemnts. 
for > N make all counters equal to highest value. 

"""
def counter(N, A):
    init_array = [0] * N
    print(init_array)
    print(A)
    max_value = 0
    for i in A:
        if i <= N:
           k = i -1
           init_array[k] += 1
        else:
            max_val = max(init_array)
            j = 0
            while j < len(init_array):
                init_array[j] = max_val
                j = j + 1
    print(init_array)
    return init_array

def counter_again(N, A):
    
    init_array = [0] * N
    print(init_array)
    print(A)
    max_value = 0
    for i in A:
        if i <= N:
           k = i -1
           init_array[k] += 1
           if init_array[k] > max_value:
               max_value = init_array[k]
        else:
            init_array = [max_value] * N # reduced from N*M to N + M
            
            
    print(init_array)
    return init_array

        


    
