'''
    Explanation:
        - We can have two data structures. An array and a hashmap
        - With the array, we can easily choose a random number from it
        - With the hashmap, we can achieve an insert and removal of O(1)

        hashmap --> key = value, value = index
        array --> contains only the value

        Insert operation
            - Append value to the end of the array
            - Add value-index pair to the hashmap

        Delete operation
            - Get index of item to be deleted from the hashmap
            - Get the last item in the array
            - Move the last item in the hashmap to where the item to be deleted is
            - Remove the last item

        TC - GetRandom function = O(1). Insert and Delete functions = O(1) on average and O(n) in the worst-case scenario when the operation exceeds the capacity of currently allocated array/hashmap and invokes space reallocation.
        SC - O(n) to store the items
'''

import random

class RandomizedSet:
    def __init__(self):
        self.hash_map = dict()
        self.array_list = []
        
    def insert(self, val: int) -> bool:
        if val in self.hash_map: return False
        self.array_list.append(val)
        self.hash_map[val] = len(self.array_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map: return False
        
        index = self.hash_map[val]
        last_item = self.array_list[-1]
        
        # get the last item in the array list and copy the last item to the index
        self.array_list[index], self.hash_map[last_item] = last_item, index
        
        # remove the last item in the array_list and remove the entry containing the key equal to the value to be removed in the hash_map
        self.array_list.pop()
        del self.hash_map[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.array_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()