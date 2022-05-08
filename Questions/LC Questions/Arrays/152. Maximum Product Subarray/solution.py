def maxProduct(nums):
    # [2,3,-2,4]
    
    maxOverallProd = maxAtEveryIndex = minAtEveryIndex = nums[0]
    
    for i in range(len(nums)):     
        temp = maxAtEveryIndex
        
        maxAtEveryIndex = max(nums[i], max(maxAtEveryIndex * nums[i], minAtEveryIndex * nums[i]))
        
        minAtEveryIndex = min(nums[i], min(temp * nums[i], minAtEveryIndex * nums[i]))

        maxOverallProd = max(maxOverallProd, maxAtEveryIndex)
    
    return maxOverallProd

# print(maxProduct([2,3,-2,4]))
# print(maxProduct([-2,0,-1]))