class Bit:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def updateTree(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += (i & -i)
    
    def getSum(self, i):
        res = 0

        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = Bit(len(nums))
        self.nums = nums

        for i, v in enumerate(nums):
            self.tree.updateTree(i + 1, v)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.tree.updateTree(index + 1, diff)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.getSum(right + 1) - self.tree.getSum(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)