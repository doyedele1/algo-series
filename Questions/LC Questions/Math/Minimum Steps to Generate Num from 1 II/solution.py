# TC - O(2^n)
def solution1(n):
    if n == 1: return 0
    elif n % 2 == 0: return 1 + solution1(n // 2)
    else: return 1 + min(solution1(n + 1), solution1(n - 1))
# print(solution1(15))

'''
    Initialize steps = 0
    While number is greater than one, perform the following,
        count++ for each iteration
        if num % 2 == 0, perform division
        else if num % 4 == 3, perform increment
        else perform decrement (as odd % 4 is either 1 or 3)
    return count;

    TC - O(log n)
'''
def solution2(n):
    if n == 1: return 0

    steps = 0

    while n > 1:
        if n % 2 == 0: n //= 2

        # n == 3 --> special case where we decrement by 1
        elif n % 4 == 1 or n == 3: n -= 1
        else: n += 1
        steps += 1

    return steps
# print(solution2(7))