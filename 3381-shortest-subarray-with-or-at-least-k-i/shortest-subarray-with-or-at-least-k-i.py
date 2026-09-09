class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        minLen = math.inf

        for i in range(len(nums)):
            value = 0
            for j in range(i, len(nums)):
                value = value | nums[j]
                if value >= k:
                    minLen = min(minLen, j-i+1)
                    break
        print(minLen)
        if minLen == math.inf:
            return -1
        else:
            return minLen