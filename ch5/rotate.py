# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# 12:28

def solution(A, K):
    if A: 
        i = 0
        while i < K:
            A = rotate_once(A)
            i = i +1
        
    return A

"""
def rotate_once(actual):
    temp = actual[len(actual)-1]
    i = 1
    while i < len(actual)-1:
        temp1 = actual[i + 1]
        actual[i +1] = actual[i]
        actual[i] = temp
        i = i +1
    return actual
"""

# Using function's inbuilt capability

def rotate_once(actual):
    if actual:
        temp = []
        temp.append(actual[len(actual)-1])
        i = 0
        while i < len(actual)-1:
            temp.append(actual[i])
            i = i +1
        return temp
    else:
        return actual