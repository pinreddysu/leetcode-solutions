class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.optimalSolution(nums)
    def optimalSolution(self, nums):
        #Two pointer-B: move both pointers in same direction
        l = 0
        r = 1

        while r < len(nums):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l+=1
            r+=1
        return l+1