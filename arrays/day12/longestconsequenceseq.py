# title: Longest Consecutive Sequence
# description: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# difficulty: Medium

class Solution(object):
    def longestConsecutive(self, nums):
        nums=set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                length = 1
                while num + length in nums:
                    length+=1
                longest = max(longest,length)
        return longest
    
# The idea is to use a set to store the numbers for O(1) look-up time.
# We iterate through each number in the set and check if it is the start of a sequence  
# (i.e., if the previous number is not in the set). If it is, we then count the length of
# the consecutive sequence starting from that number. We keep track of the maximum length found
# and return it at the end.
#core logic-- set + while loop