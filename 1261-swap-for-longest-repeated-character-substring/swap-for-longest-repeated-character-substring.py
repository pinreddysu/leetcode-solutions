class Solution:
    def maxRepOpt1(self, text: str) -> int:
        l = 0
        r = 0
        maxLen = 0
        hashArr = [0]* 26

        while r < len(text):
            hashArr[ord(text[r]) - ord('a')] += 1

            while r-l+1 - max(hashArr) > 1:
                hashArr[ord(text[l])- ord('a')] -= 1
                l+=1
            
            if r-l+1 - max(hashArr) <= 1 and r-l+1 != len(text):
                maxLen = max(maxLen, r-l+1)
            
            r+=1
        print(maxLen)
        return maxLen