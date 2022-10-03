def getEncryptedNumber(numbers):
    n = len(numbers)
    if n < 3: return numbers
    
    count = 1
    while numbers:
        if count == n:
            n -= 1
            count = 1
            numbers.pop(0)
        if n == 2: return numbers
        _sum = (numbers.pop(0) + numbers[0]) % 10
        numbers.append(_sum)
        count += 1