from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.list = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.list[idKey] = value
        
        if self.pointer < idKey:
            return []
        
        else:
            while self.pointer < len(self.list) and self.list[self.pointer] is not None:
                self.pointer += 1
            return self.list[idKey:self.pointer]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


'''
    Explanation:
    - If the current index is less than the incoming index, the we have to return an empty list
    - Else , we have to return an sliced list from the incoming index to the first index where there is no insertion till yet.
    
    - Initialize a list of size n with None
    - Maintain the current index with self.ptr
    - For every insert call, with idKey, value
        - Assign the list[idKey-1] to the value # Since array is 0-index reduce 1
        - Check if the current index is less than incoming index(idKey-1) and return []
        - Else return sliced list from incoming index(idKey-1) till we do not encounter None.
'''