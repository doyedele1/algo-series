'''
    Explanation:
        1. Check three or more candies to be crushed in rows and tag them
        2. Check three or more candies to be crushed in columns and tag them
        3. Dropping the candies

        - Steps 1 & 2: * This is an issue when considering rows --> [3,1,1,1,1,5] = [3,0,0,0,0,5] (not correct)
                                                                     1
                                                                     1

                                                                  [3,-1,-1,-1,-1,5] (correct)

        Can we check for rows and columns simultaneously? Yes. We can use a slider of three at a time and check for the absolute values of the three integers. If the absolute values are the same, then we can change the integers to negative.

        - Step 3: Dropping -  we can go column by column bottom-up. The move zeros algorithm can apply here. Whenever we see a non-negative number, we want to swap with the corresponding value of the current index of a negative number and turn the rest to 0

        TC - O(m*n)-squared. m is the number of rows and n is the number of columns in a board. We need O(m*n) to scan the board and we might crush only 3 candies repeatedly
        SC - O(1). The board is modified in place
'''

from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # To check for empty board
        if not board: board
        
        # To assume the board is stable
        done = True
        
        # To check for rows and tag them
        for row in range(len(board)):
            for col in range(len(board[row]) - 2):
                first_num = abs(board[row][col])
                second_num = abs(board[row][col+1])
                third_num = abs(board[row][col+2])
                # We want to tag the three numbers when they are equal and when they are not equal to 0
                if first_num == second_num and second_num == third_num and first_num != 0:
                    board[row][col] = -first_num
                    board[row][col+1] = -second_num
                    board[row][col+2] = -third_num
                    done = False
        
        # To check for columns and them
        for row in range(len(board) - 2):
            for col in range(len(board[0])):
                first_num = abs(board[row][col])
                second_num = abs(board[row+1][col])
                third_num = abs(board[row+2][col])
                if first_num == second_num and second_num == third_num and first_num != 0:
                    board[row][col] = -first_num
                    board[row+1][col] = -second_num
                    board[row+2][col] = -third_num
                    done = False
        
        # To drop candies that match
        if not done:
            for col in range(len(board[0])):
                # Move all non-negative numbers down
                j = len(board) - 1
                for row in range(len(board) - 1, -1, -1):
                    if board[row][col] > 0:
                        board[j][col] = board[row][col]
                        j -= 1

                # Replace the rest to 0s
                for row in range(j, -1, -1):
                    board[row][col] = 0


        return board if done else self.candyCrush(board)