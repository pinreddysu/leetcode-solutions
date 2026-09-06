class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        r = 0 
        maxLen = 0
        hashMap = [0]*26

        while r < len(s):
            hashMap[ord(s[r]) - ord('a')] += 1

            while hashMap[ord(s[r]) - ord('a')] > 2:
                hashMap[ord(s[l]) - ord('a')] -= 1
                l+=1
            
            if hashMap[ord(s[r]) - ord('a')] <= 2:
                maxLen = max(maxLen, r-l+1)
            
            r+=1
        return maxLen