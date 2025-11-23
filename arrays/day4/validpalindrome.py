# @valid palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

def isPalindrome(self, s): 
        s_new = s.replace(" ","")
        s_new = s_new.lower()
        s_new = ''.join(c for c in s_new if c.isalnum())
        if s_new == s_new[::-1]
            return True
        return False
        

        