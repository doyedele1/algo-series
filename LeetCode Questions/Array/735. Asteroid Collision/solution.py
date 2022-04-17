'''
    Explanation:
        - TC: O(n) where n is the number of asteriods. Stack append and pop is O(1)
        - SC: O(n) where n is the number of asteroids left in the stack
'''

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        
        while i < len(asteroids):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while len(stack) != 0 and 0 < stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
            i += 1
        
        return stack

#         stack = []
        
#         for asteroid in asteroids:
#             while stack and asteroid < 0 < stack[-1]:
#                 if stack[-1] < -asteroid:
#                     stack.pop()
#                     continue
#                 elif stack[-1] == -asteroid:
#                     stack.pop()
#                 break
#             else:
#                 stack.append(asteroid)
#         return stack