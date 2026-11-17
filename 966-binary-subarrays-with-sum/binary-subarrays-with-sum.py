class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # return self.bruteForceSolution(nums, goal)
        #return self.slidingWindowSolution(nums, goal) - self.slidingWindowSolution(nums, goal-1)
        return self.preFixSumSolution(nums, goal)
    def bruteForceSolution(self, nums, goal):
        maxLen = 0
        count = 0
        for i in range(len(nums)):
            sumVal = 0
            for j in range(i, len(nums)):
                sumVal += nums[j]
                if sumVal == goal:
                    count+=1
                if sumVal > goal:
                    break
        return count
    
    def slidingWindowSolution(self, nums, goal):
        if goal == -1:
            return 0
        
        sumVal = 0
        l, r = 0, 0
        count = 0
        while r < len(nums):
            sumVal += nums[r]

            while sumVal > goal:
                sumVal -= nums[l]
                l+=1
            if sumVal <= goal:
                count += r-l+1
            r+=1
        return count
    
    def preFixSumSolution(self, nums, goal):
        #return count -> freq
        preFixSumHash = {0:1}
        currentSum = 0
        count = 0

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum - goal in preFixSumHash:
                count += preFixSumHash[currentSum - goal]
            
            preFixSumHash[currentSum] = preFixSumHash.get(currentSum, 0) + 1
        
        return count
        


       