class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xorValue = 0

        for i in nums:
            xorValue = xorValue ^ i
        print(xorValue)
        return xorValue