class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        return self.betterSolution(nums, k)

    def bruteForceSolution(self, nums, k):
        subArrayLength = 0
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product < k:
                    subArrayLength += 1
                else:
                    break
        print(subArrayLength)
        return subArrayLength
    
    def betterSolution(self, nums, k):
        l = 0
        r = 0
        product = 1
        maxSubArrays = 0

        while r < len(nums):
            product *= nums[r]
            
            while product >= k and l < len(nums):
                product /= nums[l]
                l+=1
            
            maxSubArrays += r-l+1

            r+=1
        return maxSubArrays


        