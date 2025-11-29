# title: Top K Frequent Elements
# description: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# difficulty: Medium

class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1

        count=[[] for _ in range(len(nums)+1)]
        
        for key, value in freq.items():
            count[value].append(key)

        res=[]
        for i in range(len(count) -1,-1,-1):
            for num in count:
                res.append(num)
                if len(res) == k:
                    return res
                
#so we are using bucket sort to sort the elements based on their frequency
#first we fo frequency count using a dictionary, then create an array of buckets where index represents frequency
#then we iterate from the end of the bucket array to get the most frequent elements
