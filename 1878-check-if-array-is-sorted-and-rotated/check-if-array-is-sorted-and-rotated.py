class Solution:
    def check(self, nums: List[int]) -> bool:
        arrayB = [0]*len(nums)
        rotatedPos = 0

        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                pass
            else:
                rotatedPos = i
        
        rotation = len(nums) - rotatedPos
        for i in range(0, len(nums)):
            arrayB[(i+rotation) % len(nums)] = nums[i]
        
        for i in range(1, len(arrayB)):
            if arrayB[i-1] <= arrayB[i]:
                pass
            else:
                return False
        return True
