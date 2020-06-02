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

def mushrooms(A, k, m):

    n = len(A)
    result = 0
    pref = prefix_sums(A)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        # You cannot go beyond k + m -2*p got it. 
        # n - 1 understood as it is n -01
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    
    return result

def count_div(A, B, K):
    
    if A == B:
        q, r = divmod(A, B)
        if r == 0:
            return 1
        else: 
            return 0
    C = B + 1
    count = 0
    for i in range(A, C):
        if i % K == 0:
            count = count + 1
    
    return count


def compute_dna(S,P, Q):
    s_to_num = {
        'A' : 1,
        'C' : 2,
        'G' : 3,
        'T' : 4
    }
    
    len_of_arrays = len(P)
    i = 0 
    min = 5
    min_dnas = []
    while i < len_of_arrays:
        my_range = (P[i], Q[i])
        k = my_range[0]
        while k <= my_range[1]:
            # print("translation", s_to_num[S[k]])
            if s_to_num[S[k]] < min:
                min = s_to_num[S[k]]
            k = k + 1
        min_dnas.append(min)
        # print(min_dnas)
        min = 5
        
        i =  i + 1
    #print(min_dnas)
    return min_dnas

def set_character(last_seen, char):
    

def compute_dna_effecient(S,P, Q):
    s_to_num = {
        'A' : 1,
        'C' : 2,
        'G' : 3,
        'T' : 4
    }
    last_seen = {
        
        'A' : [-1]*len(S),
        'C' : [-1]*len(S),
        'G' : [-1]*len(S),
        'T' : [-1]*len(S)
    }
    print(last_seen)
    for char  in range(len(S)):
        set_character(cahr, last_seen)

    print(last_seen)
