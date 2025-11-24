# @title: Sort Colors
# @difficulty: Medium

class Solution(object):
    def sortColors(self, nums):
        # count how many 0,1,2 are there
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)

        # rewrite nums in sorted order
        nums[:] = [0]*c0 + [1]*c1 + [2]*c2
uk.ngiui