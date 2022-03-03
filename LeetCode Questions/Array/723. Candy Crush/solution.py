'''
    Explanation:
        - Major steps to determine which candies to crush,
            1. Check three or more candies to be crushed in rows
            2. Check three or more candies to be crushed in columns
            3. Dropping the candies
            
            Steps 1 & 2: * This is an issue when considering columns --> [3,1,1,1,1,5] = [3,0,0,0,0,5]
            Can we check for rows and columns simultaneously? Yes. We can use a slider of three at a time and check for the absolute values of the three integers. If the absolute values are the same, then we can change the integers to negative.
            
            Step 3: Dropping -  we can go column by column bottom-up. The move zeros algorithm can apply here. Whenever we see a non-negative number, we want to swap with the corresponding value of the current index of a negative number and turn the rest to 0
            
            
            TC - O(m*n)-squared. m is the number of rows and n is the number of columns in a board. We need O(m*n) to scan the board and we might crush only 3 candies repeatedly
            SC - O(1). The board is modified in place
'''

from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # to check for potential errors
        if not board: board
        
        # to assume the board is good
        done = True
        
        # to check for rows
        for r in range(len(board)):
            for c in range(len(board[r]) - 2):
                first_num = abs(board[r][c])
                second_num = abs(board[r][c+1])
                third_num = abs(board[r][c+2])
                if first_num == second_num and second_num == third_num and first_num != 0:
                    board[r][c] = -first_num
                    board[r][c+1] = -second_num
                    board[r][c+2] = -third_num
                    done = False
        
        
        # to check for columns
        for r in range(len(board) - 2):
            for c in range(len(board[0])):
                first_num = abs(board[r][c])
                second_num = abs(board[r+1][c])
                third_num = abs(board[r+2][c])
                if first_num == second_num and second_num == third_num and first_num != 0:
                    board[r][c] = -first_num
                    board[r+1][c] = -second_num
                    board[r+2][c] = -third_num    
                    done = False
        
        
        # to drop candies that match
        if not done:
            for c in range(len(board[0])):
                # move all non-negative numbers down
                j = len(board) - 1
                for r in range(len(board) - 1, -1, -1):
                    if board[r][c] > 0:
                        board[j][c] = board[r][c]
                        j -= 1

                # replace the rest to 0s
                for r in range(j, -1, -1):
                    board[r][c] = 0

        return board if done else self.candyCrush(board)