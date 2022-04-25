# TC - O(nlogn), SC - O(1)
def solution1(arr, b):
    arr.sort()

    for num in arr:
        if num == b:
            b *= 2
    
    return b

# TC - O(n), SC - O(n)
def solution2(arr, b):
    nums = set()

    for i in range(len(arr)):
        nums.add(arr[i])
    print(nums)

    while b in nums:
        b *= 2

    return b

# print(solution1([1,2,4,11,12,8], 2)) # 16
# print(solution1([1,2,3,1,2], 1)) # 4
# print(solution1([1,1,1], 1)) # 2
# print(solution1([2,4,5,6,8], 1)) # 1

# print(solution2([1,2,4,11,12,8], 2)) # 16
# print(solution2([1,2,3,1,2], 1)) # 4
# print(solution2([1,1,1], 1)) # 2
# print(solution2([2,4,5,6,8], 1)) # 1