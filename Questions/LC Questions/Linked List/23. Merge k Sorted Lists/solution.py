'''
    Explanation: 5 -> 7 -> 3 -> 8
        Brute force: 
            Merge 5 and 7
            5 -> 7

            Merge 3, 5 and 7
            3 -> 5 -> 7

            Merge 5, 7, 3 and 8. We have to iterate through the whole ll to find where to put 8 - not efficient. 
            TC: O(kn) - we have to iterate through every k list to merge
            3 -> 5 -> 7 -> 8

        Optimal:
            Merge 5 and 7
            5 -> 7

            Merge 3 and 8
            3 -> 8

            Merge 5 and 7 & 3 and 8
            3 -> 5 -> 7 -> 8

            Another example: If lists = [[1,4,5],[1,3,4],[2,6]]
            l1 = [1,4,5]
            l2 = [1,3,4]
            Merge l1 and l2 -> [1,1,3,4,4,5]

            l1 = [2,6]
            l2 = None
            Merge l1 and l2 -> [2,6]

            lists = [[1,1,3,4,4,5], [2,6]] - we are not done merging
            l1 = [1,1,3,4,4,5]
            l2 = [2,6]
            Merge l1 and l2 -> [1,1,2,3,4,4,5,6]

            lists = [[1,1,2,3,4,4,5,6]] - we are done merging, so return lists[0]

            TC: O(nlogk). Instead of iterating through k list, we only have to iterate log k times
            SC: O(1)
'''
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists or len(lists) == 0:
            return None
        
        def mergeTwoLists(l1 , l2):
            dummy = ListNode(-1)
            temp = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2 
                    l2 = l2.next
                temp = temp.next
            temp.next = l1 or l2
            return dummy.next
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # if length of list is odd, l2 could be out of bound 
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergeTwoLists(l1, l2))   
            lists = mergedLists
        return lists[0]