class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subArraysWithK(nums,k) - self.subArraysWithKMinusOne(nums, k)
    def subArraysWithK(self, nums, k):
        l =0
        r = 0
        hashMap = {}
        count = 0

        while r < len(nums):
            if nums[r] not in hashMap.keys():
                hashMap[nums[r]] = 1
            else:
                hashMap[nums[r]] += 1
            
            while len(hashMap.keys()) > k:
                hashMap[nums[l]] -= 1
                if hashMap[nums[l]] == 0:
                    hashMap.pop(nums[l])
                l+=1
            
            if len(hashMap.keys()) <= k:
                count += r-l+1
                r+=1
        # print(count)
        return count
    def subArraysWithKMinusOne(self, nums, k):
        l =0
        r = 0
        hashMap = {}
        count = 0

        while r < len(nums):
            if nums[r] not in hashMap.keys():
                hashMap[nums[r]] = 1
            else:
                hashMap[nums[r]] += 1
            
            while len(hashMap.keys()) > k-1:
                hashMap[nums[l]] -= 1
                if hashMap[nums[l]] == 0:
                    hashMap.pop(nums[l])
                l+=1
            
            if len(hashMap.keys()) <= k-1:
                count += r-l+1
                r+=1
        # print(count)
        return count
        