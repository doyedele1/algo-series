def getEncryptedNumber(numbers):
    n = len(numbers)
    
    if n < 3: return ''.join(str(i) for i in numbers)

    a2 = []
    while n != 2:
        for i in range(0, n-1):
            d = numbers[i] + numbers[i + 1]
            d = d % 10
            a2.append(d)
        numbers = a2
        n = len(numbers)
        a2 = []
    return ''.join(str(i) for i in numbers)

# print(getEncryptedNumber([4, 5]))