class NumArray:
    def __init__(self, nums: List[int]):
        self.cumFreqArr = []
        curr = 0

        for num in nums:
            curr += num
            self.cumFreqArr.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.cumFreqArr[left - 1] if left > 0 else 0
        rightSum = self.cumFreqArr[right]
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)