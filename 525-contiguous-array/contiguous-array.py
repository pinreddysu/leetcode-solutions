class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        preFixHash = {0: -1}

        maxLen = 0 
        preSum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                preSum -= 1
            else:
                preSum += nums[i]
            
            if preSum in preFixHash:
                maxLen = max(maxLen, i - preFixHash[preSum])
            else:
                preFixHash[preSum] = i
            # print(maxLen)
        return maxLen