'''
    Explanation:
        - To know the closest points to the origin, we can mathematically use the distance between two points formula.
        - For point [1,3], dist = (1-0)squared + (3-0)squared = 10
            - We don't need to take the square root, we just need to take the absolute difference between x and y, square it and add them together - to know which dist is closer to the origin
        
        To find the kth closest point,
        
        First approach - Sorting
            - Sort first after computing the dist. Use the value to sort the entire list of dist

            TC - O(n logn)
        
        Second approach - MinHeap
            - [10, 1, 3], [8, -2, 2]
            - Run the function heapify, to take the above in the minheap
            - We want to pop from the list k times and append the coordinate to result
            
            TC - O(k logn)
'''


from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            min_heap.append([dist, x, y])
            
        heapq.heapify(min_heap)
        while k:
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1
            
        return res