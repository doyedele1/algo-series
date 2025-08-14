class Solution1:
    def largestGoodInteger(self, num: str) -> str:
        possible_good_integers = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]

        for good_integer in possible_good_integers:
            if good_integer in num:
                return good_integer
        return ""
    
class Solution2:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = ''

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                max_digit = max(max_digit, num[i])

        return max_digit * 3