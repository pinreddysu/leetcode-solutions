class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.bruteForceSolution(nums)
        self.optimizedSolution(nums)

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
    
    def optimizedSolution(self, nums):
        l = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                l = i
                break
        if l != -1:
            r = l+1
            while r < len(nums):
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                r+=1
        print(nums)
        