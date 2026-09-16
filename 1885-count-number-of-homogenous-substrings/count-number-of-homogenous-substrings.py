class Solution:
    def countHomogenous(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        hashArray =[0]*26

        while r < len(s):
            hashArray[ord(s[r]) - ord('a')] += 1

            while s[l] != s[r]:
                hashArray[ord(s[l])- ord('a')] -= 1
                l+=1
            
            if s[l] == s[r]:
                count += r-l+1
            r+=1
        return count% (10**9 + 7)