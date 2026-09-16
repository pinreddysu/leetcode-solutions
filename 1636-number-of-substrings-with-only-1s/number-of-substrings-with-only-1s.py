class Solution:
    def numSub(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        zeros = 0

        while r < len(s):
            if s[r] == '0':
                zeros+=1
            
            while zeros > 0:
                if s[l] == '0':
                    zeros-=1
                l+=1
            
            if zeros <= 0:
                count += r-l+1
            r+=1
        return count%(10**9 +7)
    