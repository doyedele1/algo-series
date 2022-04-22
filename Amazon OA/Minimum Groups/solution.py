def minimumGroups(arr, k):
    arr.sort()
    start = 0
    if(len(arr) == 0): return 0
    
    count = 1;
    for i in range(len(arr)):
        if(arr[i] - arr[start] > k):
            count += 1
            start = i
    return count;

print(minimumGroups([1,13,6,8,9,3,5], 4))