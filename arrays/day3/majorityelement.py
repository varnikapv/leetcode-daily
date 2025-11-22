# title: Majority Element   
# description: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# difficulty: Easy

def majorityElement(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] +=1
            else:
                seen[num]=1
            if seen[num] > len(nums) // 2:
                return num
            

# Example usage:
# nums = [3,2,3]    output: 3
#here we are using dictionary, in order to not the count as well as the value and at last we are checking if the count is greater than n/2 then we return that value.