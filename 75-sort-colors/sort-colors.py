class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.betterSolution(nums)
        self.optimalSolution(nums)

    def bruteForceSolution(self, nums):
        nums.sort()
    
    def betterSolution(self, nums):

        zeros = 0
        ones = 0
        twos = 0

        for i in nums:
            if i == 0:
                zeros+=1
            elif i == 1:
                ones+=1
            else:
                twos+=1
        
        for i in range(zeros):
            nums[i] = 0
        for j in range(ones):
            nums[zeros+j] = 1
        
        for k in range(twos):
            nums[zeros+ones+k] = 2
        print(nums)
    
    def optimalSolution(self, nums):
        low, mid, high = 0, 0, len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        