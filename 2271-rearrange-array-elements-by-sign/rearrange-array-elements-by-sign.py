class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives = []
        negatives = []
        for i in nums:
            if i > 0:
                positives.append(i)
            elif i < 0:
                negatives.append(i)
        
        for i in range(len(nums)):
            if i %2 == 0:
                nums[i] = positives[i//2]
            else:
                nums[i] = negatives[i//2]
        print(nums)
        return nums