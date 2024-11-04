'''
    [1,2,3]
    [1,1,2]
'''

def findNumOfPairs(a, b):
    a = sorted(a)
    b = sorted(b)
    m = len(a)
    n = len(b)

    i, j, res = 0, 0, 0

    while i < m and j < n:
        if a[i] > b[j]:
            res += 1
            i += 1
            j += 1
        else:
            i += 1
    return res

print(findNumOfPairs([1, 2, 3], [1, 2, 1]))
print(findNumOfPairs([1, 2, 3, 4, 5], [6, 6, 1, 1, 1]))
print(findNumOfPairs([2, 3, 3], [3, 4, 5]))