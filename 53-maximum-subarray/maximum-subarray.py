class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # return self.bruteForceSolution(nums)
        return self.optimalSolution(nums)
    def bruteForceSolution(self, nums):
        maxSum = -math.inf
        for i in range(len(nums)):
            sumVal = 0
            for j in range(i, len(nums)):
                sumVal += nums[j]
                maxSum = max(maxSum, sumVal)
        return maxSum
    
    def optimalSolution(self, nums): #Kadane's Algorithm
        maxSum = -math.inf
        sumVal = 0

        for i in nums:
            sumVal += i
            maxSum = max(maxSum, sumVal)
            if sumVal < 0:
                sumVal = 0
        return maxSum