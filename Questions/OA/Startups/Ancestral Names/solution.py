def romanToInt(s):
    res = 0
    dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

    for i in range(len(s)):
        if i + 1 < len(s) and dict[s[i+1]] > dict[s[i]]:
            res -= dict[s[i]]
        
        else:
            res += dict[s[i]]
            
    return res
    
def sort_roman(names):
    res = []
    for name in names:
        n, num = name.split()
        num = romanToInt(num)
        res.append((n, num, name))
    res.sort(key = lambda x: [x[0], x[1]]) # res here is the array of tuples of name, number and name + roman
    return list(map(lambda x: x[2], res))

# print(sort_roman(["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"]))