class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # return self.bruteForceSolution(nums, goal)
        l=0
        r=0
        count= 0
        sumVal = 0
        while r < len(nums):
            sumVal += nums[r]
            while sumVal > goal:
                sumVal -= nums[l]
                l+=1

            if sumVal <= goal:
                count += r-l+1

            r+=1
        val = self.betterSolution(nums, goal)
        return count - val
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
    
    def betterSolution(self, nums, goal):
        count = 0
        l = 0
        r = 0
        sumVal = 0
        temp = 0

        if goal -1 ==-1:
            return 0
        while r < len(nums):
            sumVal += nums[r]
            while sumVal > goal-1:
                sumVal -= nums[l]
                l+=1

            if sumVal <= goal-1:
                temp += r-l+1

            r+=1
        return temp
        


       