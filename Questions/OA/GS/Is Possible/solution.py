def isPossible(a, b, c, d):
        while c >= a and d >= b:
            if c == d: break
            elif c > d:
                if d > b: c %= d
                else:
                    if (c - a) % d == 0: return "Yes"
                    else: return "No"
            else:
                if c > a: d %= c
                else:
                    if (d - b) % c == 0: return "Yes"
                    else: return "No"

        if c == a and d == b: return "Yes"
        else: return "No"