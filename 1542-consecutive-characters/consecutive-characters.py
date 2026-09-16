class Solution:
    def maxPower(self, s: str) -> int:
        l = 0
        r = 0
        hashArray = [0]*26
        maxF = 0

        while r < len(s):
            hashArray[ord(s[r]) - ord('a')] +=1
            
            while s[r] != s[l]:
                hashArray[ord(s[l]) - ord('a')] -= 1
                l+=1
            
            if s[r] == s[l]:
                maxF = max(maxF, max(hashArray))

            r+=1
        return maxF