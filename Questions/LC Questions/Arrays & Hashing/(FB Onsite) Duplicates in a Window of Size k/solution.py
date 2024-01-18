'''
    Explanation:
        - Create an empty hashmap
        - Initialize a window_start pointer to 0

        - Iterate through the array
            - Get the window_size and create a hashmap of the array
            - If the window_size is equal to k and the size of the hasmap is not the same as k, then return true
            - Else, delete the number at the window_start from the hashmap and increment the window_start pointer
            - Repeat the above steps until the end of the array is reached
        - Return false

        - TC: O(n)
        - SC: O(n)
'''

import collections

def solution(arr, k):
    hash_map = collections.defaultdict(int)
    window_start = 0

    for i in range(len(arr)):
        window_size = (i - window_start) + 1
        hash_map[arr[i]] += 1

        if window_size == k:
            if k != len(hash_map):
                return True

            hash_map[arr[window_start]] -= 1
            if hash_map[arr[window_start]] == 0:
                del hash_map[arr[window_start]]
            window_start += 1
    
    return False

# print(solution([3, 4, 1, 4, 5, 7, 2], 3))
# print(solution([3, 4, 1, 9, 5, 7, 2], 3))