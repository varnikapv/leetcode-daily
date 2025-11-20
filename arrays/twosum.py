# DAY 1

# @title Two Sum
# @description Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
# @difficulty Easy  


#time complexity: O(n)
#space complexity: O(n)

def twoSum(self, nums, target):
    seen={}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i ]
        else:
            seen[num]=i