def solutionD(n: int, nums):
    
    while '0' in nums:
        nums.remove('0')
    
    return nums


n = 8
nums = '-1 0 0 1 2 -1 -4 0'.split()

print(solutionD(n, nums))
