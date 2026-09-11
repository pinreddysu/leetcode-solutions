class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashArr = [0] * 256
        minLen = math.inf
        count = 0
        sIndex = -1
        l = 0
        r = 0

        if len(t) > len(s):
            return ""

        for i in t:
            hashArr[ord(i) - ord('a')] += 1
        
        while r < len(s):
            if hashArr[ord(s[r]) - ord('a')] > 0:
                count+=1
            hashArr[ord(s[r]) - ord('a')] -= 1

            while count == len(t):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l
                hashArr[ord(s[l]) - ord('a')] += 1
                if hashArr[ord(s[l]) - ord('a')] > 0:
                    count -= 1
                l+=1
            r+=1
        if sIndex == -1:
            return ""
        return s[sIndex: sIndex+minLen]
