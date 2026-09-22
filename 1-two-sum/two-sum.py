class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return self.optimalSolution(nums, target)
    def optimalSolution(self, nums, target):
        #Prefix sum
        hashMap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashMap.keys():
                return [i, hashMap[target-nums[i]]]
            hashMap[nums[i]] = i
        