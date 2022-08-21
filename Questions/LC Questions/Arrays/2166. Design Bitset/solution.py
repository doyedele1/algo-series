# Using two arrays. One for main array of 0s, and the other for flipped array
class Bitset1:
    
    def __init__(self, size: int):
        self.lookup = [0] * size
        self.flipped = [1] * size
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.lookup[idx] == 0:
            self.lookup[idx] = 1
            self.ones += 1
            self.flipped[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.lookup[idx] == 1:
            self.lookup[idx] = 0
            self.ones -= 1
            self.flipped[idx] = 1

    def flip(self) -> None:
        self.lookup, self.flipped = self.flipped, self.lookup
        self.ones = len(self.lookup) - self.ones

    def all(self) -> bool:
        return len(self.lookup) == self.ones

    def one(self) -> bool:
        return self.ones >= 1

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(str(i) for i in self.lookup)

# Using one array of 0s and a boolean flag for the flipped bits
class Bitset2:
    def __init__(self, size: int):
        self.lookup = [0] * size
        self.ones = 0
        self.flipped = False

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.lookup[idx] == 1:
                self.ones += 1
                self.lookup[idx] = 0
        else:
            if self.lookup[idx] == 0:
                self.ones += 1
                self.lookup[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.lookup[idx] == 0:
                self.ones -= 1
                self.lookup[idx] = 1
        else:
            if self.lookup[idx] == 1:
                self.ones -= 1
                self.lookup[idx] = 0

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = len(self.lookup) - self.ones  

    def all(self) -> bool:
        return self.ones == len(self.lookup)

    def one(self) -> bool:
        return self.ones >= 1

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flipped: return ''.join([str(0 if i else 1) for i in self.lookup])
        else: return ''.join([str(i) for i in self.lookup])

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()