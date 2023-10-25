'''
    Explanation I: Using an array of strings
        * The idea is to move pointer from a filled position to the next empty position
        
        insert, 3, cccc
            ["", "", "cccc", "", ""]
             0                      return []
            
        insert, 1, aaaa
            ["aaaa", "", "cccc", "", ""]
                     1                  return ["aaaa"]
        
        insert, 2, bbbb
            ["aaaa", "bbbb", "cccc", "", ""]
                                      4     return ["bbbb", "cccc"]
        
        insert, 5, eeee
            ["aaaa", "bbbb", "cccc", "", "eeee"]
                                     4          return [""]
                                    
        insert, 4, dddd
            ["aaaa", "bbbb", "cccc", "dddd", "eeee"]
                                                    outside        return ["dddd", "eeee"]
        
        TC: O(n)
        SC: O(n) for the list array

    Explanation II: Using a hashmap
        pointer = 1, seen = {}
    
        seen = {3: "cccc"}, res = []
        seen = {1: "aaaa", 3: "cccc"}, res = ["aaaa"], seen = {3: "cccc"}
        seen = {2: "bbbb", 3: "cccc"}, res = ["bbbb", "cccc"], seen = {}
        seen = {5: "eeee"}, res = []
        seen = {4: "dddd", 5: "eeee"}, res = ["dddd", "eeee"], seen = {}
        
        TC: O(1)
        SC: O(n) for seen hashmap
'''

from typing import List

class OrderedStream1:
    def __init__(self, n: int):
        self.pointer = 0
        self.list = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        pointer, list = self.pointer, self.list

        idKey -= 1
        list[idKey] = value
        
        while pointer < len(list) and list[pointer]:
            pointer += 1
        return list[idKey:pointer]

class OrderedStream2:
    def __init__(self, n: int):
        self.pointer = 1
        self.seen = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.seen[idKey] = value
        
        res = []
        
        while self.pointer in self.seen:
            res.append(self.seen[self.pointer])
            del self.seen[self.pointer]
            self.pointer += 1
        
        return res        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)