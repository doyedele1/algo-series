def findLargest(nums):
    quickSort(nums, 0, len(nums)-1)
    return str(int("".join(map(str, nums)))) 

def quickSort(nums, l, r):
    if l >= r:
        return 
    pos = partition(nums, l, r)
    quickSort(nums, l, pos-1)
    quickSort(nums, pos+1, r)

def compare(num1, num2):
    return str(num1) + str(num2) > str(num2) + str(num1)
    
def partition(nums, l, r):
    low = l
    while l < r:
        if compare(nums[l], nums[r]):
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low

print(findLargest([3, 30, 34, 5, 9]))