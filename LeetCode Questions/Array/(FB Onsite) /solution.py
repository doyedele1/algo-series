def pairClosestToK(nums, k):
    diff = float("inf")
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if abs(sum - k) < diff:
            res_left = left
            res_right = right
            diff = abs(sum - k)
        
        if sum < k: left += 1

        else: right -= 1

    return nums[res_left] + nums[res_right]


print(pairClosestToK([4,16,28,37,42,56,63,89,124,245], 101)) # 100
print(pairClosestToK([10, 22, 28, 29, 30, 40], 54)) # 52
print(pairClosestToK([1, 3, 4, 7, 10], 15)) # 14