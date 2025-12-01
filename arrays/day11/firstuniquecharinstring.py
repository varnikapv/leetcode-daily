# title: First Unique Character in a String
# description: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# difficulty: Easy

class Solution(object):
    def firstUniqChar(self, s):
        seen = {}
        for i in s:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1

        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i

        return -1
    
# The idea is to use a dictionary to count the occurrences of each character in the string.
# We first iterate through the string and populate the dictionary with character counts.
# Then, we iterate through the string again and return the index of the first character with a count of 1.
# If no such character is found, we return -1.