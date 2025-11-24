'''
    Explanation:
        [0, 1, 1]

        For 0, yes it is divisible by 5
        Then we shift 0 to the left and add 1. For 01, no it is not divisible by 5
        Then we shift 01 to the left and add 1. For 011, no it is not divisible by 5

        That's the solution in Python.

        But let's solve a potential bug in other languages because we will get integer overflow in those languages
        Consider an array with many 1s in front (could be of length 10 up to 32)
        
        Case 1: [1,1,1...,1,_,_,_]. The three slots is divisible by 5. 101.
        [1,1,1...,1,1,0,1], let's call this curr
        curr % 5 will be 0 because 101 is divisible by 5 already

        Hence, we can replace the entire curr with 0 and it won't impact the next number in next subarray. But why?
        If we consider the next number in the next subarray:
        (curr << 1) + num = 2 * curr + num. 2 * curr will still be divisible by 5 since curr << 1 is already divisible by 5. 
        So we don't need curr anymore, hence why we replace with 0 and we can focus on the new number

        Case 2: [1,1,1...,1,_,_,_]. The three slots is not divisible by 5 and it is less than 5. 011.
        [1,1,1...,1,0,1,1]
        011 % 5 = 3 % 5 = 3

        With this observation, we can also get rid of all the initial 1s because they won't help us to determine if the three slots (3) is divisible by 5

        Case 3: [1,1,1...,1,_,_,_]. The three slots is not divisible by 5 and it is greater than 5. 111.
        [1,1,1...,1,1,1,1]
        111 % 5 = 7 % 5 = 2
        If we shift 111 to the left, we get 2 * 2 which is 4 and 4 % 5 is still 4

        With this case, we can observe that if we shift a number that is not originally divisible by 5,
        It still won't cause a case where it is divisible by 5 because when we shift a number, we multiply that number by 2

        TC: O(n), SC: O(1)
'''
from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        curr = 0

        for num in nums:
            # curr = (curr << 1) + num
            # to solve integer overflow bug in other languages because curr can be greater than 32 in the test cases
            curr = ((curr << 1) + num) % 5
            res.append(curr % 5 == 0)
        return res