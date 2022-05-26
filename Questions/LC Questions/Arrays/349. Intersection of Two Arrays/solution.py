class Solution:
    def intersection(self, nums1, nums2):
        seen = {}
        res = []
        
        for num in nums1:
            if num in seen: seen[num] += 1
            else: seen[num] = 1
        # print(seen)
        
        for num in nums2:
            if num in seen and seen[num] > 0:
                res.append(num)
                seen[num] = 0
    
        return res