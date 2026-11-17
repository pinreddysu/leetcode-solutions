class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        return self.optimizedSolution(nums)
    def preFixSuffixSolution(self, nums):
        preFixSum = [0]
        sufFixSum = [0]

        for i in range(len(nums)):
            preFixSum.append(preFixSum[i]+nums[i])
            sufFixSum.insert(0,sufFixSum[0] + nums[len(nums)-1-i])
        

        for i in range(len(nums)):
            if preFixSum[i+1] - nums[i] == sufFixSum[i] - nums[i]:
                return i
        
        return -1

    def optimizedSolution(self, nums):
        totalSum = sum(nums)
        currentSum = 0
        for i in range(len(nums)):
            # print(currentSum, totalSum - currentSum - nums[i])
            if currentSum == totalSum - currentSum - nums[i]:
                return i
            currentSum += nums[i]
        return -1
