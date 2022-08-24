'''
    Explanation:
        - We can have two data structures. An array and a hashmap that maps to a set of values
        - With the array, we can easily choose a random number from it
        - With the hashmap, we can achieve an insert and removal of O(1)

        hashmap --> key = value, value = set of indices
        array --> contains only the value

        Insert operation
            - Add values-index pair to the hashmap
            - Append value to the end of the array

            - If length of that set in the hashmap is equal to 1, then it means the value was not present in the hashmap before, so return true

        Delete operation
            [1, 2, 3, 4, 5]. Task: remove 3
            [1, 2, 5, 4, 5]. Then remove the last element which is the second 5 --> [1, 2, 5, 4]

            - Get index of item to be deleted from the hashmap
            - Get the last item in the array
            - Move the last item in the hashmap to where the item to be deleted is
            - Remove the last item

        TC - GetRandom function = O(1). 
            Insert and Delete functions = 
                O(1) on average
                O(n) in the worst-case scenario when the operation exceeds the capacity of currently allocated array/hashmap and invokes space reallocation.
        SC - O(n) to store the items
'''

from collections import defaultdict
from random import randint, choice

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
        
        # Get the index of the value to be removed from the hashmap and the last item in the array list
        index, lastItem = self.hashMap[val].pop(), self.arrayList[-1]
        
        self.arrayList[index] = lastItem
        self.hashMap[lastItem].add(index)
        
        self.hashMap[lastItem].discard(len(self.arrayList) - 1)
        # the remove() method raises an error if the item to be removed does not exist; the discard() method does not
        self.arrayList.pop()
        
        return True

    def getRandom(self) -> int:
        # return choice(self.arrayList)
        randomIndex = randint(0, len(self.arrayList) - 1)
        return self.arrayList[randomIndex]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()