def closestNumbers(numbers):
    if len(numbers) <= 1:
        print("")
        return

    numbers = sorted(map(int, numbers))
    diff = float("inf")
    prev = numbers.pop(0)

    for i in numbers:
        if i - prev < diff:
            ans = [prev, i]
            diff = i - prev
        elif i - prev == diff:
            ans.append(prev)
            ans.append(i)
        prev = i
    ans.sort()
    
    for i in range(0, len(ans), 2):
        print(ans[i], ans[i + 1])

closestNumbers([6, 2, 4, 10])