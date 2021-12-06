class Solution:
    def findKthLargest(self, nums, k):
        
        def partition(pivot_idx, left, right, nums):
            pivot_val = nums[pivot_idx]
            
            # Move pivot to end
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            # Move all smaller elements to the left
            i = left
            j = left
            for j in range(left, right):
                if nums[j] < pivot_val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    
            # Move pivot to its final position. i.e. where the element should rightly be when sorted
            nums[right], nums[i] = nums[i], nums[right]
            
            return i
        
        def quick_select(left, right, nums, target):
            pivot_idx = (left + right) // 2
            
            # Find pivot's final position after sorted
            pivot_idx = partition(pivot_idx, left, right, nums)
            
            if pivot_idx == target: return nums[target]
            elif pivot_idx < target: return quick_select(pivot_idx + 1, right, nums, target)
            else: return quick_select(left, pivot_idx - 1, nums, target)
                
        return quick_select(0, len(nums) - 1, nums, len(nums) - k)