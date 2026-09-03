class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # maxLen = 0

        # for i in range(len(s)):
        #     hashArr = [0] * 26
        #     for j in range(i, len(s)):
        #         hashArr[ord(s[j]) - ord('A')] +=1

        #         if j-i+1 -(max(hashArr)) <=k:
        #             maxLen = max(maxLen, j-i+1)
        #         else:
        #             break
        # print(maxLen)
        # return maxLen
    
        l = 0
        r = 0
        maxLen = 0
        hashArr = [0] * 26

        while r < len(s):
            hashArr[ord(s[r]) - ord('A')] += 1

            while r - l + 1 - max(hashArr) > k:
                hashArr[ord(s[l]) - ord('A')] -= 1
                l+=1
            
            if r-l+1 - max(hashArr) <= k:
                maxLen = max(maxLen, r-l+1)
                r+=1
        print(maxLen)
        return maxLen