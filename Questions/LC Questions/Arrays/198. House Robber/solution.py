'''
    Explanation:
        - [1,2,3,1]
            Decision Tree
        If we decide to rob houses 1 and 2,
             1               2
            / \             /
           3   1           1
        The recurrence relation: rob = max(nums[0] + rob[2:n], rob[1:n])

        [house_one, house_two, n, n+1, ...]

        Example 1: [1, 2, 3, 1]
            house_one = 1, house_two = max(1,2) = 2
            If we rob house n, we have two choices:
                Choice 1: n + house_one = 3 + 1 = 4
                Choice 2: maximum until house_two = 2
            
            If we rob house n+1, we have two choices:
                Choice 1: (n+1) + maximum until house_two = 1 + 2 = 3
                Choice 2: maximum until house n = 4

        Example 2: [2, 7, 9, 3, 1]
            house_one = 2
            house_two = max(2,7) = 7
            house_n = (9+2) or 7 = 11
            house_n+1 = (3+7) or (11) = 11
            house_n+2 = (1+11) or (11) = 12
        
    TC: O(n)
    SC: O(1)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        house_one, house_two = 0, 0

        for num in nums:
            curr = max(num + house_one, house_two)
            house_one = house_two
            house_two = curr
        return house_two