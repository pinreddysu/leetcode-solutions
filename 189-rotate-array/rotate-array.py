class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.bruteForceSolution(nums, k)

    def bruteForceSolution(self, nums, k):
        rotations = k % len(nums)
        rightKElements = nums[-rotations:]
        if rotations > 0:
            for i in range(len(nums)-rotations-1, -1, -1):
                nums[i+rotations] = nums[i]
            
            for i in range(rotations):
                nums[i] = rightKElements[i]
            print(nums)
