# TC: O(log-squared n for sorting)
# SC: O(log n) 
# where log n is the number of digits. But number of digits is at most 10
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        str_n = sorted(str(n))

        for i in range(30):
            power_of_2 = 1 << i # 2 ** i

            sorted_power_of_2 = sorted(str(power_of_2))

            if str_n == sorted_power_of_2:
                return True
        return False