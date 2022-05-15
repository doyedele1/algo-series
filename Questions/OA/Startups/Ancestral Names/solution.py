def roman_to_int(s:str):
    rom_to_int_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sub_map = {'IV': 4, 'IX':9, 'XL': 40, 'XC': 90, 'CD':400, 'CM': 900}
    summation = 0
    idx = 0

    while idx < len(s):
        if s[idx:idx+2] in sub_map:
            summation += sub_map.get(s[idx:idx+2])
            idx += 2
        else:
            summation += rom_to_int_map.get(s[idx])
            idx += 1
    return summation
    
def sort_roman(names):
    name_array = []
    for name in names:
        n, num = name.split()
        num = roman_to_int(num)
        name_array.append((n, num, name))
    name_array.sort(key=lambda x: [x[0], x[1]])
    return list(map(lambda x:x[2], name_array))