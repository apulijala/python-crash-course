def missing_integer(A):
    max_val = max(A)
    if max_val <= 0:
        return 1
    # Let us count the elements. 
    my_range = max_val + 1
    count = [0] * my_range
    for i in A:
        if i >= 1:  # No need to store the -ve valuer can be discarded.
            count[i] += 1 # Count occurence of the array.
    
    for i in range(1, my_range):
        if count[i] == 0: # retunr it. 
            return i

    # Nothing returned. So need to return the max value + 1. as it will be smallest +ve integer
    return my_range


# Simple counting problem. With range being the max 
# value of the array.

def permutation_wrong_one(A):
    max_value = max(A)
    my_range = max_value + 1
    count = [0] * my_range

    for i in A:
        count[i] += 1
    print(count)


    for i in range(1, my_range):
       if count[i] == 0:  # handles 0 or multipoe
           return 0 # Failure here.
    
    return 1 # No non zero value. Permutation, return 1


def permutation_wrong_two(A):
    max_value = max(A)
    my_range = max_value + 1
    count = [0] * my_range
    for i in A:
        count[i] += 1
    
    for i in range(1, my_range):
        if count[i] != 1:  # handles 0 or multipoe
            return 0 # Failure here.
    
    return 1 # No non zero value. Permutation, return 1


def permutation(A):
    max_value = max(A)
    my_range = max_value + 1
    count = {}
    for i in A:
        if i in count.keys():
             count[i] += 1
        else:
            count[i] = 1
    for i in range(1, my_range):
        try:
            if count[i] != 1:  # handles 0 or multipoe
                return 0 # Failure here.
        except KeyError: # catching error is better than not in check
            return 0
    
    return 1 # No non zero value. Permutation, return 1



