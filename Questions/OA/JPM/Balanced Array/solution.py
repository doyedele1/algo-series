def solution(arr):
    n = len(arr)

    arr_sum = sum(arr)

    curr = arr[0]
    for i in range(1, n):
        if curr == arr_sum - curr - arr[i]:
            return i
        curr += arr[i]
    return