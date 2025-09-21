'''
    Explanation:
        Can we use an array?
        This means we need to have a large array to store our numbers in their index.
        From the constraints, array size can get up to 10^9
        So no, we can't use a hashmap

        Can we use a hashmap?
        Sure, we can use a hashmap. key will be the index, value will be the number
        But with find(number) method, we can't easily find value from a hashmap. We can only find key in O(1)

        Hence, we will need another hashmap which is an inverted hashmap

        Can we use a sorted set?
        With the inverted hashmap, key will be the number and value will be the index
        However, value can be more than one, as we can store a number at different indices. So to get the smallest index, we can't just use an array as that's not sorted
        So we use a sorted set as we can get the first item in the set easily in O(1)

        Let's do a dry run:
        change (5, 2)
        idx_num_map = {5: 2}
        num_idx_map = {2: 5}

        change (3, 10)
        idx_num_map = {5: 2, 3: 10}
        num_idx_map = {2: [5], 10: [3]}

        change (4, 2)
        idx_num_map = {4: 2, 5: 2, 3: 10}
        num_idx_map = {2: [5,4], 10: [3]}

        find (2)
        We check the num_idx_map, and we return the smallest idx which is 4

        change (3, 6)
        idx_num_map = {4: 2, 5: 2, 3: 10}
        num_idx_map = {2: [5,4], 10: [3]}

        Since there is a number at index 3, we replace that. 
        But before we do that, we check the num_idx_map, and delete the 3 in key of 10. 
        After deletion, if the value array is empty, we can delete the key as well

        Hence,
        idx_num_map = {4: 2, 5: 2, 3: 6}
        num_idx_map = {2: [5,4], 6: [3]}

        find (10)
        Since the number doesn't exist, return -1

        change (4, 7)
        idx_num_map = {4: 7, 5: 2, 3: 6}
        num_idx_map = {2: [5], 6: [3], 7: [4]}

        change (8, 2)
        idx_num_map = {4: 7, 5: 2, 3: 6, 8: 2}
        num_idx_map = {2: [5, 8], 6: [3], 7: [4]}

        find (2)
        We check the num_idx_map, and we return the smallest idx which is 5


        Analysing the time complexities:
        change method: O(logn). For insertion/erase in the sorted set which uses red/black tree which is a balanced binary tree
        find method: O(1). For getting the first item in the sorted set

        Overall: TC = Q * O(logn + 1) where Q is the number of queries
        
        TC: = O(Qlogn)
        SC: O(n)
'''
from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.idx_num_map = {}
        self.num_idx_map = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idx_num_map:
            num = self.idx_num_map[index]
            self.num_idx_map[num].discard(index)
            if not self.num_idx_map[num]:
                del self.num_idx_map[num]

        self.idx_num_map[index] = number
        if number not in self.num_idx_map:
            self.num_idx_map[number] = SortedSet()
        self.num_idx_map[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.num_idx_map:
            return -1
        return self.num_idx_map[number][0]
        
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)