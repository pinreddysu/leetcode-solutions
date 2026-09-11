class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxValue = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                print(nums[i], nums[j])
                if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]):
                    maxValue = max(maxValue, nums[i] ^ nums[j])
        print(maxValue)
        return maxValue