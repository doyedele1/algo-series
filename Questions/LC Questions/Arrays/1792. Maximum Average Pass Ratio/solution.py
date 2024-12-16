'''
    classes = [[1,2], [3,5], [2,2]], extraStudents = 2
    Let's first calculate increment and push to a maxheap, that way we know which class gives us the highest increment:
                    class 0       class 1       class 2
    curr_avg        0.50000       0.60000       1.00000
    new_avg         0.66667       0.66667       1.00000
    increment       0.16667       0.06667       0.00000
    max_heap = (
        -0.166667, 0
        -0.06667, 1
        -0.00000, 2
    )

    Now let's update the class that returns the maximum increment by adding an extra student
    classes = [[2,3], [3,5], [2,2]]
    Calculate increment and push to a maxheap:
                    class 0       class 1       class 2
    curr_avg        0.66667       0.60000       1.00000
    new_avg         0.75000       0.66667       1.00000
    increment       0.08333       0.06667       0.00000
    max_heap = (
        -0.08333, 0
        -0.00000, 2
        -0.06667, 1
    )

    Again let's update the class that returns the maximum increment by adding an extra student
    classes = [[3,4], [3,5], [2,2]]
    Calculate increment and push to a maxheap:
                    class 0       class 1       class 2
    curr_avg        0.75000       0.60000       1.00000
    new_avg         0.80000       0.66667       1.00000
    increment       0.05000       0.06667       0.00000
    max_heap = (
        -0.06667, 1
        -0.00000, 2
        -0.05000, 0
    )

    Final_average = ((3/4) + (3/5) + (2/2)) / 3 = 0.78333

    TC: O(klogn) + O(nlogn) = O(nlogn)
    O(klogn) for insertions and removal from the max heap
    O(nlogn) for iterating through the heap and calculating the final average pass ratio

    SC: O(n) where n is the number of classes in the max heap 
'''
from typing import List
import heapq

class Solution:
    def calc_increment(self, pass_students, total_students):
            curr_avg = pass_students / total_students
            new_avg = (pass_students + 1) / (total_students + 1)
            return new_avg - curr_avg

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []

        for i, (pass_students, total_students) in enumerate(classes):
            increment = self.calc_increment(pass_students, total_students)
            heapq.heappush(max_heap, (-increment, i))

        while extraStudents > 0:
            _, idx = heapq.heappop(max_heap)
            classes[idx][0] += 1
            classes[idx][1] += 1
            increment = self.calc_increment(classes[idx][0], classes[idx][1])
            heapq.heappush(max_heap, (-increment, idx))
            extraStudents -= 1

        final_avg = sum(c[0] / c[1] for c in classes)
        return final_avg / len(classes)