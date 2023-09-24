'''
    Explanation:
        - We can have two data structures. An array and a hashmap that maps to a set of values
            - With the array, we can easily choose a random number from it
            - With the hashmap, we can achieve an insertion and removal of O(1)

            hashmap --> key = value, value = set of indices
            array --> contains only the value

        Insert operation
            - Add value-indices pair to the hashmap
            - Append value to the end of the array

        Remove operation
            - Use the hashmap to find the index of the element to be removed & remove that index from the set
            - Use the array to find the last item

            - In the array, set the value of the removed index to be the last item
            - In the hashmap, add the removed index to the set of the last item

            - Remove the added removed index from the set

        insert(1)
            hashMap = {1: {0}}
            arrayList = [1]
        
        insert(1)
            hashMap = {1: {0, 1}}
            arrayList = [1, 1]

        insert(2)
            hashMap = {1: {0,1}, 2: {2}}
            arrayList = [1, 1, 2]
        
        remove(1)
            index = 0, lastItem = 2

            arrayList = [2, 1, 2]
            hashMap = {1: {1}, 2: {0,2}}

            hashMap = {1: {1}, 2: {0}}
            arrayList = [2, 1]

        TC - all functions: O(1)
        SC - O(n) to store the items
'''

from collections import defaultdict
from random import randint

class RandomizedCollection:
    def __init__(self):
        self.arrayList = []
        self.hashMap = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.hashMap[val].add(len(self.arrayList))
        self.arrayList.append(val)
        
        return len(self.hashMap[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.hashMap[val]: return False
        
        index, lastItem = self.hashMap[val].pop(), self.arrayList[-1]
        
        self.arrayList[index] = lastItem
        self.hashMap[lastItem].add(index)
        
        self.hashMap[lastItem].discard(len(self.arrayList) - 1)
        # the remove() method raises an error if the item to be removed does not exist; the discard() method does not
        self.arrayList.pop()

        return True

    def getRandom(self) -> int:
        randomIndex = randint(0, len(self.arrayList) - 1)
        return self.arrayList[randomIndex]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()