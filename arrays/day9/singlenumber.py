# title: Single Number
# description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# difficulty: Easy

class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res 
    
    # The idea is to use XOR operation. XOR of a number with itself is 0 and XOR of a number with 0 is the number itself.
    # So, when we XOR all the numbers together, the numbers that appear twice will cancel out and we will be left with the single number.   
# For example, if the input array is [4,1,2,1,2], the XOR operation will be:
# 0 ^ 4 = 4 
# 4 ^ 1 = 5
# 5 ^ 2 = 7
# 7 ^ 1 = 6
# 6 ^ 2 = 4
# So the output will be 4 which is the single number in the array.