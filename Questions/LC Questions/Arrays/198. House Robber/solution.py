'''
    Explanation:
        - [1,2,3,1]
            Decision Tree
        If we decide to rob houses 1 and 2,
             1               2
            / \             /
           3   1           1
        The recurrence relation: rob = max(nums[0] + rob[2:n], rob[1:n])

        1   2   3   1
        # [house_one, house_two, n, n+1, ...]
        If we rob house n, we have two choices:
            Choice 1: n + house_one
            Choice 2: maximum until house_two
        
        If we rob house n+1, we have two choices:
            Choice 1: (n+1) + maximum until house_two
            Choice 2: maximum until house n

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