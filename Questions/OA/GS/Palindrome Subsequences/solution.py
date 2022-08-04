from collections import Counter

MODULO = 10 ** 9 + 7

def getPalindromesCount(s):
    count = Counter([''])
    freqFives = 0

    for c in s:
        for item, freq in list(count.items()):
            item += c
            if len(item) < 5:
                count[item] += freq
            elif item == item[::-1]:
                freqFives += freq
    
    return freqFives % MODULO

print(getPalindromesCount("0100110"))