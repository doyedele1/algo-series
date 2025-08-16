class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)

        num_str = num_str.replace('6', '9', 1)

        return int(num_str)