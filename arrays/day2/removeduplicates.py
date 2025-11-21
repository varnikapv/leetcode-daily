# @remove duplicates from sorted array
# @description: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array
# difficulty: easy

def removeDuplicates(self, nums):
        left = 1
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left +=1
        return left

#we have to remove the duplicates, we first start with left pointer at index 1
#we iterate through the array with right pointer starting from index 1  
#whenever we find a non-duplicate element, we place it at the left pointer and increment left pointer
#finally we return the left pointer which indicates the length of the array without duplicates