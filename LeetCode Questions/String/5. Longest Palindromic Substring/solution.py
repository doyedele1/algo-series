class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        res = ""
        for i in range(len(s)):
            test = helper(i, i)
            if len(test) > len(res):
                res = test
            test = helper(i, i+1)
            if len(test) > len(res):
                res = test
        return res
    
        '''
            Explanation:
                Brute-force:
                    - Check every single possible substring inside the string
                    - TC - O(n-cube)
                More optimal
                    - Rather than having two pointers, what if we start from the middle
                    - TC: O(n-squared), SC: O(1)
        '''