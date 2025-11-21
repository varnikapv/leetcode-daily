# @Move zeroes to end of array
# @description Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
# difficulty Easy   

class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left = left + 1


#  instead of checking for the zero numbers, we check for non-zero ones and then swap it with the first element 
#  This way all non-zero elements are moved to the front and zeros are pushed to the end
