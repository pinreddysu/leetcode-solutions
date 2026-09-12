class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return self.bruteForceSolution(nums, k)
        return self.optimizedSolution(nums, k)

    def bruteForceSolution(self, nums, k):
        rotations = k % len(nums)
        rightKElements = nums[-rotations:]
        if rotations > 0:
            for i in range(len(nums)-rotations-1, -1, -1):
                nums[i+rotations] = nums[i]
            
            for i in range(rotations):
                nums[i] = rightKElements[i]
            print(nums)
    def optimizedSolution(self, nums, k):
        rotations = k % len(nums)
        def reverse(l, r):
            while l < r:
                nums[l],  nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        reverse(0, len(nums)-1)
        reverse(0, rotations-1)
        reverse(rotations, len(nums)-1)
