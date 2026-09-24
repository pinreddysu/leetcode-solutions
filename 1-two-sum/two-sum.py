class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return self.optimalSolution(nums, target)
        # return self.bruteForceSolution(nums, target)

    def bruteForceSolution(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


    def optimalSolution(self, nums, target):
        #Prefix sum
        hashMap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashMap.keys():
                return [i, hashMap[target-nums[i]]]
            hashMap[nums[i]] = i
        