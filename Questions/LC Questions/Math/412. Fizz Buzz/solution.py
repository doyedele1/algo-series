from typing import List

# TC: O(n), SC: O(1)
class StringConcatenationSolution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n + 1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)

            ans_str = ""
            if divisible_by_3:
                ans_str += "Fizz"
            if divisible_by_5:
                ans_str += "Buzz"
            if not ans_str:
                ans_str = str(i)

            ans.append(ans_str)
        return ans