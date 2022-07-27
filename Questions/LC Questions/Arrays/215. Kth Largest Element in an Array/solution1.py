'''
    k = 1, 1st largest element --> largest element, k = 2, 2nd largest element

    [3,2,1,5,6,4], k = 2 --> ans = 5, [3,2,1,5,6,4], k = 4 --> ans = 3

    [3,2,3,1,2,4,5,5,6], k = 4 --> ans = 4
        6 --> 1st
        5 --> 2nd
        5 --> 2nd
        4 ---> 4th

    Explanation I: Sorting
        - We need to sort the nums array - O(n logn). # quick sort, merge sort, O(n-squared) bubble sort, selection sort, insertion sort, radix
            - ascending order or descending order?
            - descending order --> [6, 5, 4, 3, 2, 1], k = 2
            - 2nd largest element? --> return nums[k-1]
            - TC: O(n logn), SC: O(1)
            
    Explanation II: Using a heap
        Using heaps - min heap (stores large numbers) and max heap (stores small numbers)
        [3,2,1,5,6,4]
        heap = [
                    6
                    5
        ], maximum size of heap where k = 2

        TC: O(k) + O(n logk) = O(n logk)
        SC: O(k) - space required by the heap
'''