# @title: Plus One
# @description: Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# @difficulty: Easy 

def plusOne(self, digits):
        lastInd = len(digits) - 1
        while lastInd >= 0:
            if digits[lastInd] != 9:
                digits[lastInd] = digits[lastInd] + 1
                return digits
            else:
                digits[lastInd] = 0
                lastInd -= 1
        return [1] + digits

# Example usage:
# digits = [1, 2, 3]        
# print(plusOne(None, digits))  # Output: [1, 2, 4]
# digits = [9, 9, 9]        
# print(plusOne(None, digits))  # Output: [1, 0, 0, 0] 