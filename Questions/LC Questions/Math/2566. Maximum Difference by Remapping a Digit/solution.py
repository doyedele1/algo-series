'''
    Explanation:
        To get the MAX value: Change the first non-9 digit to a 9
        To get the MIN value: Change the very first digit to a 0

        TC: O(n)
        SC: O(n) where n is the number of digits in num
'''

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        max_val = s
        for digit in s:
            if digit != '9':
                max_val = s.replace(digit, '9')
                break
        
        digit_to_change = s[0]
        min_val = s.replace(digit_to_change, '0')

        return int(max_val) - int(min_val)