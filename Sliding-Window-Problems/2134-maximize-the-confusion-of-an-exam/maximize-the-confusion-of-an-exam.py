class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        r = 0
        maxLen = 0
        hashMap = {}

        while r < len(answerKey):
            if answerKey[r] not in hashMap.keys():
                hashMap[answerKey[r]] = 1
            else:
                hashMap[answerKey[r]] += 1
            
            if r-l+1 - max(hashMap.values()) > k:
                hashMap[answerKey[l]] -= 1
                l+=1
            if r-l+1 - max(hashMap.values()) <= k:
                maxLen = max(maxLen, r-l+1)
            r+=1
        print(maxLen)
        return maxLen
