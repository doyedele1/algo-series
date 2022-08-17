# Brute-Force Solution --> TC - O(log n), SC - O(1)
class Solution1:
    def numberOfSteps(self, num: int) -> int: 
        if num == 0: return 0
        
        steps = 0
        while num > 0:
            if num % 2 == 0: num //= 2
            else: num -= 1
            steps += 1
        return steps
        
# Counting Bits --> TC - O(log n), SC - O(log n)
class Solution2:
    def numberOfSteps(self, num: int) -> int: 
        binaryEquivalent = bin(num)[2:]
        ones = binaryEquivalent.count("1")
        zeroes = len(binaryEquivalent) - ones
        return (ones * 2) + zeroes - 1