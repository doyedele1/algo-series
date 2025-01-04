from typing import List

# TC: O(n), SC: O(1)

class BruteForceSolution:
    def fizz_buzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n + 1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
    
class StringConcatenationSolution:
    def fizz_buzz(self, n: int) -> List[str]:
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
    
class HashSolution:
    def fizz_buzz(self, n: int) -> List[str]:
        ans = []
    
        fizz_buzz_hash = {
            3: "Fizz",
            5: "Buzz"
        }

        keys = [3, 5]

        for i in range(1, n + 1):
            ans_str = ""
            
            for key in keys:
                if i % key == 0:
                    ans_str += fizz_buzz_hash[key]
                    
            if not ans_str:
                ans_str = str(i)

            ans.append(ans_str)
        return ans