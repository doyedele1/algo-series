'''
    Explanation I: Sorting
        [1, 1, 1, 2, 2, 3]
        - Count the frequency of each number and store in a hashmap - {1: 3, 2: 2, 3: 1}
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
        - Count the frequency of each number and store in a hashmap
        - Initially, we could do a bucket sort of the possible numbers in the input array as key and count as value, but the input array numbers are unbounded, so this wouldn't work efficiently and the bucket sort doesn't tell us where the top k elements are
        - The bucket sort we would use for this solution will be:
            - key = frequency of each value
            - value = list of the numbers that have that particular count
            [1, 1, 1, 2, 2, 3]
            key (freq)     0        1       2       3      4       5       6
            values                  [3]     [2]     [1]
            - Why is key getting to 6? Length of the key will be the size of the input array, because in worst case, we could have [1,1,1,1,1,1] which is 6. So key will be from 0 to 6
        - We want the top k vlaues. So we can start from the end of the key list and add to the result array k times
    
        - TC: O(n) because the maximum size k could be is the length of the input array
            - If we have distinct values, [1,2,3,4,5,6], we will add the numbers to the key of 1 in O(6n) time
        - SC: O(n) for the hashmap, bucket and result array
'''

from collections import Counter
import heapq
from typing import List

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        heap = []
        countMap = {}
        res = []

        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)

        for num, freq in countMap.items():
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
        countMap = {}
        bucket = [[] for i in range(len(nums) + 1)] # + 1 so we don't go out of bound if input array = [1]
        
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
        
        for num, freq in countMap.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k: return res