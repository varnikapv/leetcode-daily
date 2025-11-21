# @title: Rotate Array
# @description: This script rotates an array to the right by a given number of steps.
# difficulty: Medium    

def rotate(self, nums, k):
        k = k % len(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        left, right = 0, k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        left,right = k, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right-=1

#notes: so im reversing the entire array first
# then reversing the first k elements
# then reversing the remaining elements from k to end of array