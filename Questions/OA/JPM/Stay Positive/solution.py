def minStart(arr):
    res, total = 0, 0

    for num in arr:
        total += num
        res = min(res, total)

    return 1 - res