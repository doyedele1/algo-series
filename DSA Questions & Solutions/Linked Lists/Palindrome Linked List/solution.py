# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # TC - O(n), SC - O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        start = 0
        end = len(nums) - 1
        while(start < end):
            if(nums[start] != nums[end]):
                return False
            start += 1
            end -= 1
        return True

    # TC - O(n), SC - O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        # 2 --> 3 --> 7 --> 3 --> 2
    
        # find middle element using the slow pointer
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        # slow = node of 7
        # fast = node of second 2

        # 2 --> 3 --> 2 --> 3 -- 7
        # reversing the second part of the linked list
        prev = None
        while(slow != None):
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        # left = node of first 2
        # right = node of second 2
        # check for palindrome
        left = head
        right = prev
        while(right != None):
            if(left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True
            