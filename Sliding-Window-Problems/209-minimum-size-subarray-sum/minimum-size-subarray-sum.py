class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        What is my window?
        -> My window is variable and it is integers that are >= target
        What makes it invalid?
        -> When my window reaches the sum of subarray > target and len of current
        window is greater than min window that we found 
        When do I move right?
        -> We expand it to add integers and to find min window
        When do I move left?
        -> We move left when target <= subarray and if current window > min window
        What does my hashmap/count store?
        -> We don't use hashMap we just use sum varialbe to increment or decrement
        the value when moving right or left
        Am I finding one window or counting multiple?
        -> we are finding one window which has min subarray length
        '''
        # return self.bruteForceSolution(target, nums)
        return self.betterSolution(target, nums)
    def bruteForceSolution(self, target, nums):
        minLen = math.inf
        for i in range(len(nums)):
            targetSum = 0
            for j in range(i, len(nums)):
                targetSum += nums[j]
                if targetSum >= target:
                    minLen = min(minLen, j-i+1)
                    break
        return 0 if minLen == math.inf else minLen

    def betterSolution(self, target, nums):
        l = 0
        r = 0
        minLen = math.inf
        targetSum = 0

        while r < len(nums):
            targetSum += nums[r]

            while targetSum >= target:
                minLen = min(minLen, r-l+1)
                targetSum -= nums[l]
                l+=1
                
            r+=1

        print(minLen)
        return 0 if minLen == math.inf else minLen