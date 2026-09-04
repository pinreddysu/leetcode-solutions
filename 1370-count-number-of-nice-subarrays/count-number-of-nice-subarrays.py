class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #Strategy 3
        # print(self.subArraysAtMostK(nums,k), self.subArraysAtMostKMinusOne(nums,k))
        return self.subArraysAtMostK(nums,k) - self.subArraysAtMostKMinusOne(nums,k)
    def subArraysAtMostK(self, nums, k):
        l = 0
        r = 0
        hashMap = {}
        count = 0
        sumOdd = 0

        while r < len(nums):
            if nums[r] not in hashMap.keys():
                hashMap[nums[r]] = 1
                if nums[r] % 2 ==1:
                    sumOdd +=1
            else:
                hashMap[nums[r]] +=1
                if nums[r] %2 == 1:
                    sumOdd +=1
            
            while sumOdd > k:
                hashMap[nums[l]] -= 1
                if nums[l] % 2==1:
                    sumOdd-=1
                l+=1
            
            if sumOdd <= k:
                count+=r-l+1
            r+=1
        print(count)
        return count
    def subArraysAtMostKMinusOne(self, nums, k):
        l = 0
        r = 0
        hashMap = {}
        count = 0
        sumOdd = 0

        while r < len(nums):
            if nums[r] not in hashMap.keys():
                hashMap[nums[r]] = 1
                if nums[r] % 2 ==1:
                    sumOdd +=1
            else:
                hashMap[nums[r]] +=1
                if nums[r] %2 == 1:
                    sumOdd +=1
            
            while sumOdd > k-1:
                hashMap[nums[l]] -= 1
                if nums[l] % 2==1:
                    sumOdd-=1
                l+=1
            
            if sumOdd <= k-1:
                count+=r-l+1
            r+=1
        print(count)
        return count


        