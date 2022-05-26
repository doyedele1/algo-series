'''
    Explanation:
        [-1, 3, 2, -3]
            - stack = [-1], asteroid = -1
            - stack = [-1, 3], asteroid = 3
            - stack = [-1, 3, 2], asteroid = 2
            - stack = [-1], asteroid = 0

        TC: O(n) where n is the number of asteriods. Stack append and pop is O(1)
        SC: O(n) where n is the number of asteroids left in the stack
'''

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            
            # We can only start the collision when these conditions are met
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]
                # Asteroid is going to win here, so remove the top element in the stack
                if diff < 0: stack.pop()
                # The top of the stack is going to win and asteroid is to be destroyed
                elif diff > 0: asteroid = 0
                # When both will be destroyed
                else:
                    asteroid = 0
                    stack.pop()
            
            # Only add to the stack if asteroid is positive or negative
            if asteroid: stack.append(asteroid)
                
        return stack