class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return self.betterSolution(nums, k)
    
    def bruteForceSolution(self, nums, k):
        #Subarray with constant window
        maxAverage = -math.inf
        for i in range(len(nums)-k+1):
            sumSubArray = 0.0
            for j in range(i, i+k):
                sumSubArray += nums[j]
            maxAverage = max(maxAverage, sumSubArray/k)
        print(maxAverage)
        return maxAverage

    def betterSolution(self, nums, k):
        maxAverage = -math.inf
        l = 0
        r = k
        sumSubArray = sum(nums[:k])
        maxAverage = sumSubArray / k
        print(maxAverage)

        while r < len(nums):
            if l < r:
                sumSubArray -= nums[l]
                l+=1
            sumSubArray += nums[r]
            print(r)
            maxAverage = max(maxAverage, sumSubArray/k)
            r+=1
        return maxAverage





