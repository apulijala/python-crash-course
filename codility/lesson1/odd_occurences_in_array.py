def solution(A):
    found = {}
    for num in A:
        if num in found.keys():
            found[num] = found[num] + 1
        else:
            found[num] = 1
    
    for key, val in found.items():
        if val % 2 == 1:
            return key


    """
    Time complexity is still N2
    for num in A:
        if A.count(num) % 2 == 1:
            return num
    """
    """
    initial solution 14 mins. but failed because of time complexity. Scored 66%f
    while A:
        val = A.pop(0)
        count = A.count(val)
        actcount = count + 1 # for the one that is removed. 
        if actcount % 2 == 1:
            return val
        while val in A: # remove all the occurences
            A.remove(val)
    """    