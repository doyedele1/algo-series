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