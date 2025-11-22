# @title: Missing Number
# @description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# @difficulty: Easy

class Solution(object):
    def missingNumber(self, nums):
        k = len(nums)
        nums_set = set(nums)

        for i in range(0, k+1):
            if i not in nums_set:
                return i
# Example usage:
# nums = [3,0,1]    output: 2   
# so here we are converting the list into set so that we can have O(1) time complexity for searching the missing number. Then we are iterating from 0 to n and checking if the number is present in the set or not, if not we return that number.