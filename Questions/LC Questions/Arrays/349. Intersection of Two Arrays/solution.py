'''
    Explanation I: Hash Set
        - Clarifying questions to ask: duplicates, negative values, single value lists, 0s, empty lists
        nums1 = [1,2,2,1], nums2 = [2,2]
        
        nums1 = set1 = (1,2)
        nums2 = set2 = (2)
        - We then iterate over the smallest set which is nums2. For every nums in set2, if we find them in set1, we add to the result array
        
        - TC: O(m + n) where m is the length of nums1 and n is the length of nums2. 
            - O(m) to convert nums1 to set1
            - O(n) to convert nums2 to set2
            - O(1) to look up the set
        - SC: O(m + n) worst case is when all elements in the arrays are different
        
    Explanation II: Sorting and Two Pointers
        nums1 = [1,2,2,1], nums2 = [2,2]
        nums1 = [1, 1, 2, 2]
        nums2 = [2, 2]
        
        - i = 0, j = 0, move i
        - i = 1, j = 0, move i
        - i = 2, j = 0, add the number 2 to res array and move both i and j
        - i = 3, j = 1, add the number 2 to the res array again
        
        - return set(res)
        
        - TC: O(m logm + n logn)
        - SC: O(log m + log n) to O(m + n) depending on the sorting algorithm used
'''

from typing import List


class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def helper(set1, set2):
            return [nums for nums in set1 if nums in set2]
        
        set1, set2 = set(nums1), set(nums2)
        
        if len(set1) < len(set2): return helper(set1, set2)
        else: return helper(set2, set1)
                
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]: j += 1
            elif nums1[i] < nums2[j]: i += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
                
        return set(res)             