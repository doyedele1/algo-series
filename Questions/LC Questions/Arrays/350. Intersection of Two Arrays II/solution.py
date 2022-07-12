'''
    Explanation I: Hash Map
        - We used a hash set for question 349, we use a hash map here
        - We check the array sizes and use a hashmap on the smaller array to reduce memory usage when one of the arrays is very large
        - Create a freqCounter of nums1
        - Initialize result pointer k to zero
        - Iterate through nums2
            - If num in freqCounter and count is positive,
                - Copy num to nums1[k] and move result pointer k
                - Decrement count in freqCounter
        - Return first k elements of nums1
        
        - TC: O(n + m)
        - SC: O(min(m, n)) for the smaller array
        
    Explanation II: Sorting and Two Pointers - when the input is sorted or when output needs to be sorted
        nums1 = [1,2,2,1], nums2 = [2,2]
        nums1 = [1, 1, 2, 2]
        nums2 = [2, 2]
        
        - i = 0, j = 0, k = 0, move i
        - i = 1, j = 0, k = 0, move i
        - i = 2, j = 0, k = 0, add the number 2 to the k position which is 0 and move both i, j and k
        - i = 3, j = 1, k = 1, add the number 2 to the k position which is 1 and return first k elements in nums[1]
        
        - return res
        
        - TC: O(m logm + n logn)
        - SC: O(log m + log n) to O(m + n) depending on the sorting algorithm used
'''


class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        
        freqCounter = {}
        k = 0
        for num in nums1:
            if num in freqCounter: freqCounter[num] += 1
            else: freqCounter[num] = 1
        
        for num in nums2:
            if num in freqCounter and freqCounter[num] > 0:
                freqCounter[num] -= 1
                nums1[k] = num
                k += 1
        
        return nums1[:k]


from typing import List

class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j, k = 0, 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]: j += 1
            elif nums1[i] < nums2[j]: i += 1
            else:
                nums1[k] = nums1[i]
                k += 1
                i += 1
                j += 1
                
        return nums1[:k]