from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_idx = m + n - 1
        
        # iterating in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_idx] = nums1[m - 1]
                m -= 1
            else:
                nums1[last_idx] = nums2[n - 1]
                n -= 1
            last_idx -= 1
            
        # considering edge case - leftover elements in nums2
        while n > 0:
            nums1[last_idx] = nums2[n - 1]
            n -= 1
            last_idx -= 1
        

        '''
            Explanation:
                - Start iterating with a pointer from the last index of nums1
                - Compare the largest integers in both nums1 and nums2 and replace the end of nums1 which should be 0 to that largest integer
                - Move pointers of both nums1 and nums2
                
                TC - O(m + n)
                SC - O(1)
        '''