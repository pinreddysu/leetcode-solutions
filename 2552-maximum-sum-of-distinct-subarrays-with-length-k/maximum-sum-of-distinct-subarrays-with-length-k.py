class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        hashMap = {}
        currSum = 0
        maxSum = 0

        while r < len(nums):
            currSum += nums[r]
            if nums[r] not in hashMap.keys():
                hashMap[nums[r]] = 1
            else:
                hashMap[nums[r]] += 1
            
            if r-l+1 == k: 
                if len(hashMap.keys()) == k:
                    maxSum = max(maxSum, currSum)

                hashMap[nums[l]] -= 1
                currSum -= nums[l]
                if hashMap[nums[l]] == 0:
                    hashMap.pop(nums[l])
                l+=1
            r+=1

        print(maxSum)
        return maxSum