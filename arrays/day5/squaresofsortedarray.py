# Title: Squares of a Sorted Array
# Difficulty: Easy
# Description: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        new=[]
        for i in nums:
            new.append(i**2)
        return sorted(new)
    