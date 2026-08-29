class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return self.bruteForceSolution(target, nums)
        return self.betterSolution(target, nums)
    #Bruteforce does not work because of time limit exceeded
    def bruteForceSolution(self, target, nums):
        minLength = math.inf

        for i in range(len(nums)):
            targetSum = 0
            for j in range(i,len(nums)):
                targetSum += nums[j]
                if targetSum >= target:
                    print(j,i)
                    minLength = min(minLength, j-i+1)
                    break
        if(minLength == math.inf):
            return 0
        return minLength

    def betterSolution(self, target, nums):
        l, r, targetSum = 0, 0, 0
        minLength = math.inf

        while l < len(nums):
            if r < len(nums):
                targetSum += nums[r]
            while targetSum >= target:
                minLength = min(minLength, r-l+1)
                targetSum-=nums[l]
                l+=1
            
            if targetSum < target and r == len(nums):
                l+=1
            
            if r != len(nums):
                r+=1
        if minLength == math.inf:
            print(0)
            return 0
        else:
            print(minLength)
            return minLength