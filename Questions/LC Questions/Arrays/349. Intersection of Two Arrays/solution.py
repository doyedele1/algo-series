'''
    Clarifying questions to ask: duplicates, negative values, single value lists, 0s, empty lists

    Explanation I: Sorting and Two Pointers
        nums1 = [1,2,2,1], nums2 = [2,2]
        nums1 = [1, 1, 2, 2]
        nums2 = [2, 2]
        
        i = 0, j = 0, move i
        i = 1, j = 0, move i
        i = 2, j = 0, add the number 2 to res set and move both i and j
        i = 3, j = 1, add the number 2 to the res set again
        
        return list(res)
        
        TC: O(mlogm + nlogn)
        SC: O(m + n) depending on the sorting algorithm used

    Explanation II: Two Hash Sets
        nums1 = [1,2,2,1], nums2 = [2,2]
        
        nums1 = set1 = (1,2)
        nums2 = set2 = (2)
        We then iterate over the smallest set which is nums2. 
        For every nums in set2, if we find them in set1, we add to the result array
        
        TC: O(m + n) where m is the length of nums1 and n is the length of nums2. 
            O(m) to convert nums1 to set1
            O(n) to convert nums2 to set2
            O(1) to look up the set
        SC: O(m + n) worst case is when all elements in the arrays are different

    Explanation III: One Dictionary
        TC: O(m + n)
        SC: O(n) for the seen dictionary
'''

from typing import List

class SortingSolution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        m = len(nums1)
        n = len(nums2)
        res = set()
        i, j = 0, 0
        
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return list(res)
    
class TwoSetsSolution:
    def intersection_of_two_sets(self, set1, set2):
            return [x for x in set1 if x in set2]
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        
        if len(set1) < len(set2):
            return self.intersection_of_two_sets(set1, set2)
        else:
            return self.intersectionOfTwoSets(set2, set1)
        
class OneDictionarySolution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = []

        for num in nums1:
            seen[num] = 1
        
        for num in nums2:
            if num in seen and seen[num] == 1:
                res.append(num)
                seen[num] = 0
        
        return res