class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
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