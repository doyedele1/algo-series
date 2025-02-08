'''
    Explanation: Hashmap Solution
        Observation:
            To know if (x + y) is divisible by z,
            (x + y) % z = 0

            Let, x % z be R1 and y % z be R2

            If x is 140, y = 100 and z = 60,
            R1 = 140 % 60 = 20
            R2 = 100 % 60 = 40
            Then, R1 + R2 must be z. 20 + 40 = 60 in this case

            Another example: 
            If x is 0, y = 0 and z = 60,
            R1 = 0 % 60 = 0
            R2 = 0 % 60 = 0
            Then, R1 + R2 = 0

            Hence, we can conclude the following:
            0 <= R1 + R2 <= z

            With this observation, we can come up with a solution:
            time = [30, 20, 150, 100, 40]
            
            1. Create a remainder array from the input array
            remainder = [30, 20, 30, 40, 40]

            2. Convert the remainder to a hashmap so that it can be easy to access elements in O(1) time
            remainder = {30: 2, 20: 1, 40: 2}

            3.
            If we see a value less than 30, we can find the number of valid pairs by looking for the difference which is 60 - number
            So for example, 20, difference will be 40
            Then we can do number of times 20 appear * number of times 40 appear

            You might ask yourself, why are we not doing for values greater than 30.
            It's because we will be creating duplicates.
            Pair (20, 40) is the same as pair (40, 20). Hence, we only need one.
            And values less than 30 are mirrored and will have the same processing as values greater than 30
            
            Special cases:
            If we see a 0 or a 30, then the numer of valid pairs we can create will be:
            n * (n - 1) // 2 where n is the number of times either 0 or 30 appear in the map

        With these observations, we can come up with solutions 1 and 2
        
        Solution I: With hashmap
        TC: O(n)
        SC: O(n)

        Solution II: Another optimal solution using array
        TC: O(n + divisor)
        SC: O(n + divisor)
'''
from typing import List
from collections import Counter

class SolutionI:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_arr = []

        for num in time:
            remainder_arr.append(num % 60)

        count = 0
        remainder = Counter(remainder_arr)

        for num in remainder:
            if num == 0 or num == 30:
                n = remainder[num]
                count += (n * (n - 1) // 2)
            elif num < 30:
                count += (remainder[num] * remainder[60 - num])
        return count

class SolutionII:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_arr = [0] * 60

        for num in time:
            remainder_arr[num % 60] += 1

        count = 0
        # Special cases
        count += (remainder_arr[0] * (remainder_arr[0] - 1) // 2)
        count += (remainder_arr[30] * (remainder_arr[30] - 1) // 2)

        for i in range(1, 30):
            count += remainder_arr[i] * remainder_arr[60 - i]
        return count