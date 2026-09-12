class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.bruteForceSolution(nums)

        
    def bruteForceSolution(self, nums):
        nonZeros = []

        for i in nums:
            if i != 0:
                nonZeros.append(i)
        
        for i in range(len(nonZeros)):
            nums[i] = nonZeros[i]

        for i in range(len(nonZeros), len(nums)):
            nums[i] = 0
        print(nums)
        