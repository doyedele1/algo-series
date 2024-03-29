from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC: O(n), SC: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] != nums[end]:
                return False
            start += 1
            end -= 1
        return True

# TC: O(n), SC: O(1)
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # 2 --> 3 --> 7 --> 3 --> 2
    
        # find middle element using the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow = node of 7
        # fast = node of second 2

        # 2 --> 3 --> 2 --> 3 -- 7
        # reversing the second part of the linked list
        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        # left = node of first 2
        # right = node of second 2
        # check for palindrome
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True