# @title:Intersection of Two Arrays
# @description:Given two arrays, write a function to compute their intersection.
# @difficulty: easy

def intersection(self, nums1, nums2):
        seen=set(nums1)
        res = []
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res

#we use a set to store elements of the first array
#we then iterate through the second array, if an element is in the set, we add it to the result and remove it from the set to avoid duplicates in the result        
#finally we return the result array