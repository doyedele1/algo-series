'''
    Explanation:
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
'''


from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def helper(set1, set2):
            return [nums for nums in set1 if nums in set2]
        
        set1, set2 = set(nums1), set(nums2)
        
        if len(set1) < len(set2): return helper(set1, set2)
        else: return helper(set2, set1)
                