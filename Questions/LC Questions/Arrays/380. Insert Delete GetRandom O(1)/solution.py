'''
    Explanation:
        - We can have two data structures. An array and a hashmap
            - With the array, we can easily choose a random number from it
            - With the hashmap, we can achieve an insertion and removal of O(1)

            hashmap -> key = value, value = index
            array -> contains only the value

        Insert function
            - Append value to the end of the array
            - Add value-index pair to the hashmap

        Remove function
            [1, 2, 3, 4, 5]
            - Use the hashmap to find the index of the element to be removed
            - Use the array to find the last item

            - In the array, set the value of the removed index to be the last item
            - In the hashmap, set the value of the last item to be the removed index

            - Remove the last item in the array
            - Remove the value to be removed from the hashmap

         insert(1)
            arrayList = [1]
            hashMap = {1:0}

        remove(2)
            return False since 2 does not exist
        
        insert(2)
            arrayList = [1, 2]
            hashMap = {1:0, 2:1}
        
        remove(1)
            index = 0, lastItem = 2

            arrayList = [2, 2]
            hashMap = {1:0, 2:0}

            arrayList = [2]
            hashMap = {2:0}
        
        insert(2)
            return False since 2 is already in the set

        TC - all functions: O(1)
        SC - O(n) to store the items
'''

from random import randint

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
        
        self.arrayList[index], self.hashMap[lastItem] = lastItem, index
        
        self.arrayList.pop()
        del self.hashMap[val]
        
        return True

    def getRandom(self) -> int:
        # return choice(self.arrayList)
        randomIndex = randint(0, len(self.arrayList) - 1)
        return self.arrayList[randomIndex]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()