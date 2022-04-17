'''
    Explanation:
        - TC: O(n) where n is the number of asteriods. Stack append and pop is O(1)
        - SC: O(n) where n is the number of asteroids left in the stack
'''

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]
                if diff < 0: stack.pop()
                elif diff > 0: asteroid = 0
                else:
                    asteroid = 0
                    stack.pop()
            if asteroid:
                stack.append(asteroid)
        
        return stack