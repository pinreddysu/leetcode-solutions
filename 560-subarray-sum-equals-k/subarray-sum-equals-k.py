class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        preFixSum = 0
        count = 0

        for i in range(len(nums)):
            preFixSum += nums[i]

            # if preFixSum == k:
            #     count+=1
            # elif preFixSum != k:
            if preFixSum - k in hashMap.keys():
                    count += hashMap[preFixSum -k]
            if preFixSum not in hashMap.keys():
                hashMap[preFixSum] = 1
            else:
                hashMap[preFixSum] +=1
        print(count)
        return count