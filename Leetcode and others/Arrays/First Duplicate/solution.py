class Solution:
    def findDuplicate(self, nums):
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen: return nums[i]
            
            else: seen.add(nums[i])

# Floyd cycle's algorithm
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow