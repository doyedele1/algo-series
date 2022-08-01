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
        [1, 2, 3, 4, 5]. Task: remove 3
        [1, 2, 5, 4, 5]. Then remove the last element which is the second 5 --> [1, 2, 5, 4]

            - Get index of item to be deleted from the hashmap
            - Get the last item in the array
            - Move the last item in the hashmap to where the item to be deleted is
            - Remove the last item

        TC - GetRandom function = O(1). Insert and Delete functions = O(1) on average and O(n) in the worst-case scenario when the operation exceeds the capacity of currently allocated array/hashmap and invokes space reallocation.
        SC - O(n) to store the items
'''

from random import randint, choice

class RandomizedSet:
    def __init__(self):
        self.hashMap = dict()
        self.arrayList = []
        
    def insert(self, val: int) -> bool:
        if val in self.hashMap: return False

        self.arrayList.append(val)
        self.hashMap[val] = len(self.arrayList) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap: return False
        
        index = self.hashMap[val]
        lastItem = self.arrayList[-1]
        
        # Get the last item in the array list and copy the last item to the index
        self.arrayList[index], self.hashMap[lastItem] = lastItem, index
        
        # Remove the last item in the arrayList and remove the entry containing the key equal to the value to be removed in the hashMap
        self.arrayList.pop()
        del self.hashMap[val]
        
        return True

    def getRandom(self) -> int:
        return choice(self.arrayList)
        # randomIndex = randint(0, len(self.arrayList) - 1)
        # return self.arrayList[randomIndex]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()