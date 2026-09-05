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
        r = 0
        sumSubArray = 0

        while r < len(nums):
            sumSubArray += nums[r]

            if r-l+1 == k:
                maxAverage = max(maxAverage, sumSubArray/k)

                sumSubArray -= nums[l]
                l+=1
            r+=1
        return maxAverage





