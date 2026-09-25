class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # return self.bruteForceSolution(nums)
        return self.betterSolution(nums)
    def bruteForceSolution(self, nums):
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count+=1
            if count > len(nums) // 2:
                return nums[i]
    def betterSolution(self, nums):
        hashMap = {}
        for i in nums:
            if i not in hashMap.keys():
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        
        # return max(hashMap, key=hashMap.get)
        for i in hashMap.keys():
            if hashMap[i] > len(nums) // 2:
                return i