'''
    Explanation I: Sorting
        [1, 1, 1, 2, 2, 3]
        - Create a hashamp for the frequency of each number - {1: 3, 2: 2, 3: 1}
        - Create a new list where each element is a list of two values: frequency and number. [[1,3], [2,2], [3,1]]
        - Sort the list based on frequencies which is nestedList[i][0]. [[3,1], [2,2], [1,3]]
        - Get the first k numbers = [1,2]
        
        - TC: O(nlog n)
        - SC: O(n) for the hashmap and the nested lists
        
    Explanation II: Heap (maxHeap)
        - Count the frequency of each number and store in a hashmap
        - Add each pair to build a maxheap
            - Key of the maxheap = number of occurences
        - Pop from the heap exactly k times
        
        - TC: O(klog n) -- building heap with heapify - O(n). Pop from heap - O(log n), exactly k times - O(klog n)
        - SC: O(n + k). n for the hashmap, k for the heap
    
    Explanation III: Bucket Sort
    
    
        - TC: O(n)
        - SC: O(n)
'''

from collections import Counter
import heapq
from typing import List
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        heap = []
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, freq in count.items():
            heap.append((-freq, num))
        heapq.heapify(heap)
        # heap here = [(-3, 1), (-2, 2), (-1, 3)]

        while k > 0:
            freq, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        return res

class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res