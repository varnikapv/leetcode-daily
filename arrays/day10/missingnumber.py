# title: Missing Number
# description: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# difficulty: Easy

class Solution(object):
    def missingNumber(self, nums):
        seen = set(nums)
        for i in range(0, len(nums)+1):
            if i not in seen:
                return i


# The idea is to use a set to keep track of the numbers present in the array.
# Then, we iterate through the range from 0 to n (where n is the length of the array) and check for the first number that is not in the set.
# This number is the missing number and we return it.# For example, if the input array is [3,0,1], the set will be {0,1,3}.
