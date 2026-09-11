class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # return self.bruteForceSolution(nums, k)
        return self.betterSolution(nums,k)
    
    #Brute force did not work due to time limit
    def bruteForceSolution(self, nums, k):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j)<=k:
                    return True
        return False
    
    #Two Pointers
    def betterSolution(self, nums, k):
        l = 0
        r = 0
        hashMap = {}
        while r < len(nums):
            if nums[r] not in hashMap.keys():
                hashMap[nums[r]] = r
            else:
                print(hashMap)
                if abs(hashMap[nums[r]]-r) <=k:
                    return True
                else:
                    hashMap[nums[r]] = r
            r+=1
        return False
            

            


        