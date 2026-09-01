class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # maxLength = 0
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] == 0:
        #             count+=1
        #         if count <= k:
        #             maxLength = max(maxLength, j-i+1)
        #         else:
        #             break
        # print(maxLength)
        # return maxLength
        return self.optimizedSolution(nums, k)

    def optimizedSolution(self, nums, k):
        l = 0
        r = 0 
        maxLength = 0
        zeros = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <=k:
                maxLength = max(maxLength, r - l + 1)
                r += 1
        print(maxLength)
        return maxLength
        
                