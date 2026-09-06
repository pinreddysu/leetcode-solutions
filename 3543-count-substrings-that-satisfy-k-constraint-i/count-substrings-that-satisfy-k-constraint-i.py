class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hashArr = [0] * 2
        count = 0
        while r < len(s):
            hashArr[int(s[r])] +=1

            while hashArr[0] > k and hashArr[1] > k:
                hashArr[int(s[l])] -= 1
                l+=1
            
            if hashArr[0] <= k or hashArr[1] <= k:
                count += r-l+1
            r+=1
        print(count)
        return count