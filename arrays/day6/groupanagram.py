# title: group Anagrams
# difficulty: Medium
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict 
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for sr in strs:
            count = [0] * 26
            for ch in sr:
                count[ord(ch)-ord("a")] += 1 
            key=tuple(count)
            res[key].append(sr)
        return res.values()
    
# time complexity: O(n k) where n is number of strings and k is the maximum length of a string in strs