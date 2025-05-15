from typing import List

# TC: O(n), SC: O(1)
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        res = []

        if not words:
            return []

        res.append(words[0])
        last_added_group = groups[0]

        for i in range(1, n):
            curr_group = groups[i]
            if curr_group != last_added_group:
                res.append(words[i])
                last_added_group = curr_group

        return res