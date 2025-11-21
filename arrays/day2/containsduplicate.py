# @contains duplicate in array
# @description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# @difficulty: easy

def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False

#we use a set to keep track of seen elements
#we iterate through the array, if we find an element already in the set, we return True
#if we finish iterating through the array without finding duplicates, we return False