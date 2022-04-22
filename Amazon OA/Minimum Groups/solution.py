'''
    [1,13,6,8,9,3,5]
    
    [1,3,5,6,8,9,13]

    First iteration: count = 1, start = 0
    Second iteration: count = 1, start = 0
    Third iteration: count = 1, start = 0
    Fourth iteration: count = 2, start = 3
    Fifth iteration: count = 2, start = 3
    Sixth iteration: count = 2, start = 3
    Seventh iteration: count = 3, start = 6
'''

def minimumGroups(arr, k):
    arr.sort()
    start = 0
    if len(arr) == 0: return 0
    
    count = 1
    for i in range(len(arr)):
        if (arr[i] - arr[start]) > k:
            count += 1
            start = i
    return count

print(minimumGroups([1, 13, 6, 8, 9, 3, 5], 4))