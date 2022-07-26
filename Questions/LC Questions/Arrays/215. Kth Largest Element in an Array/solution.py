'''
    k = 1, 1st largest element --> largest element, k = 2, 2nd largest element

    [3,2,1,5,6,4], k = 2 --> ans = 5, [3,2,1,5,6,4], k = 4 --> ans = 3

    [3,2,3,1,2,4,5,5,6], k = 4 --> ans = 4
        6 --> 1st
        5 --> 2nd
        5 --> 2nd
        4 ---> 4th

    Explanation I: Sorting
        - We need to sort the nums array - O(n logn). # quick sort, merge sort, O(n-squared) bubble sort, selection sort, insertion sort, radix
            - ascending order or descending order?
            - descending order --> [6, 5, 4, 3, 2, 1], k = 2
            - 2nd largest element? --> return nums[k-1]
            - TC: O(n logn), SC: O(1)
            
    Explanation II: Using a heap
        Using heaps - min heap (stores large numbers) and max heap (stores small numbers)
        [3,2,1,5,6,4]
        heap = [
                    6
                    5
        ], maximum size of heap where k = 2
'''


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