def slow_leader(A):

    leader = -1
    n = len(A)
    for k in range(n):
        candidate = A[k]
        count = 0
        for i in range(0,n):
            if A[i] == candidate:
                count = count + 1

        if count >  n//2:
            return candidate
    
    return leader

def fast_leader(A):
    # First sort the array.
    A.sort()
    n = len(A)
    count = 0
    leader = -1
    candidate = A[n // 2]
    for i in range(n):
        if candidate == A[i]:
            count = count + 1
    
    if count > n//2:
        leader = candidate
    
    return leader


def golden_leader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else: 
                size += 1
    
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count = count + 1
    
    if count > n // 2:
        leader = candidate

    return leader


def solution(A):
        n = len(A)
        size = 0
        for k in range(n):
            if size == 0:
                size += 1
                value = A[k]
            else:
                if value != A[k]:
                    size -= 1
                else: 
                    size += 1
        
        candidate = -1
        if size > 0:
            candidate = value
        leader = -1
        count = 0
        for i in range(n):
            if A[i] == candidate:
                count = count + 1
        
        if count > n // 2:
            leader = candidate
        
        if leader != -1:
            for i in range(n):
                if A[i] == leader:
                    return i
            
        return -1
    



def golden_leader_simplified(A,i,j):
    n = len(A)
    size = 0
    for k in range(i, j):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else: 
                size += 1
    
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for i in range(i, j):
        if A[i] == candidate:
            count = count + 1
    
    if count > ((j -i) // 2):
        leader = candidate

    return leader


def equi_leader(A):
    n = len(A)
    count = 0
    for i in range(n-1):
        leader1 = golden_leader_simplified(A,0,i)
        leader2 = golden_leader_simplified(A,i+1,n)
        
        if leader1 == leader2:
            count  = count + 1

    return count



