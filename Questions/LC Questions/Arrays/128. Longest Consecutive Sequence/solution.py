class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in nums:
            if (num - 1) not in num_set:
                sequence_length = 0
                while (num + sequence_length) in num_set:
                    sequence_length += 1
                res = max(res, sequence_length)

        return res