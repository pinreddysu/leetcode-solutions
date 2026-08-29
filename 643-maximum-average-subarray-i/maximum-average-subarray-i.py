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

    #Better Solution: For fixed window always calculate the initial amount till window size then start r from window size to entire list and run l to r since the window is fixed because when r reaches to end the gap must be k digits to the left for fixed window
    def betterSolution(self, nums, k):
        maxAverage = -math.inf
        l = 0
        r = k
        sumSubArray = sum(nums[:k])
        maxAverage = sumSubArray / k

        while r < len(nums):
            if l < r:
                sumSubArray -= nums[l]
                l+=1
            sumSubArray += nums[r]
            maxAverage = max(maxAverage, sumSubArray/k)
            r+=1
        return maxAverage





