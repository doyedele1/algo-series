# TC: O(D) - the number of unique remainders we can have is D - 1, SC: O(D). D is the value of denominator
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        if (numerator < 0) != (denominator < 0):
            res.append("-")

        num, den = abs(numerator), abs(denominator)

        # Integer part
        res.append(str(num // den))
        remainder = num % den
        if remainder == 0:
            return "".join(res)
        
        # Decimal part
        res.append(".")
        remainders_seen = {} # {remainder: position_in_res}

        while remainder != 0:
            if remainder in remainders_seen:
                pos = remainders_seen[remainder]
                res.insert(pos, "(")
                res.append(")")
                break

            remainders_seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // den))
            remainder %= den
        return "".join(res)