def solution(A):
    # write your code in Python 3.6
    nums = {}
    for i in A:
        if i in nums.keys():
            nums[i] = nums[i] + 1
        else:
            nums[i] = 1
    
    for key, value in nums.items():
        if value % 2 == 1:
            return key
       