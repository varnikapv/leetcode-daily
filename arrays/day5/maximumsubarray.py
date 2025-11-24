# title: Maximum subarray
# difficulty: Easy
#we have to find the max subarray sum in the array

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum  
    
#time complexity: O(n)
#space complexity: O(1)
#we can also use kadane's algorithm to solve this problem   