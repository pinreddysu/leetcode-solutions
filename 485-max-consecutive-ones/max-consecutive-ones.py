class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.optimalSolution(nums)
    
    def slidingWindowSolution(self, nums):
        l = 0
        r = 0
        zeros = 0
        maxLen = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros +=1
            
            if zeros > 0:
                if nums[l] == 0:
                    zeros-=1
                l+=1
            if zeros <= 0:
                maxLen = max(maxLen, r-l+1)
            r+=1
        return maxLen

    def optimalSolution(self, nums):
        count = 0
        maxCount = 0
        for i in nums:
            if i == 1:
                count+=1
                maxCount = max(maxCount, count)
            else:
                count = 0
        return maxCount