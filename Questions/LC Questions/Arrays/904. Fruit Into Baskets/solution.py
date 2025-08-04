from typing import List

# Sliding window -> TC: O(n), SC: O(1)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = 0
        basket = {} # {fruitType: count}
        left = 0

        for right in range(n):
            fruit = fruits[right]
            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1

            res = max(res, right - left + 1)
        return res