'''
    Explanation:
        when n = 10,
            q = (1)
            Step 0:
                visited = {1}
                q = (2,0)
        
            Step 1:
                visited = {1,2}
                q = (0,4,0)
        
                visited = {1,2,0}
                q = (4,0)
        
            Step 2:
                visited = {1,2,0,4}
                q = (0,8)
        
                visited = {1,2,0,4}
                q = (8)
        
            Step 3:
                visited = {1,2,0,4,8}
                q = (16)
        
            Step 4:
                visited = {1,2,0,4,8,16}
                q = (32,5)
        
            Step 5:
                visited = {1,2,0,4,8,16,32}
                q = (5,64,10)
        
                visited = {1,2,0,4,8,16,32,5}
                q = (64,10,10)
        
            Step 6:
                visited = {1,2,0,4,8,16,32,5,64}
                q = (10,10,128,21)
        
                top = 10 which is our number
    
        TC - O(<2^steps)
        SC - hashmap: O(>steps), queue: O(>steps)
    '''

import collections

def solution1(n):
    head = 1
    steps = 0
    q = collections.deque([head])
    visited = set()
    
    while q:
        for i in range(len(q)):
            top = q.popleft()
            
            if top == n: return steps
                
            if top not in visited: visited.add(top)
        
            if top * 2 not in visited: q.append(top * 2)
        
            if top // 3 not in visited: q.append(top // 3)
        steps += 1

# print("solution1", solution1(10))

# IGNORE --> not an efficient solution, doesn't evaluate the minimum number of steps
def solution2(n):
    x = 0
    y = 0

    while n:
        temp = (2 ** x) // (3 ** y)
        if temp < n: x += 1
        elif temp > n: y += 1
        else: return x + y

# print("solution2", solution2(10))