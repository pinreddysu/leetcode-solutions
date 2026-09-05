class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        l = 0
        r = 0
        location = []
        hashMapP = {}
        hashMapS = {}
        for i in p:
            if i not in hashMapP.keys():
                hashMapP[i] = 1
            else:
                hashMapP[i] +=1
        # print(hashMapP)
        while r < len(s):
            if s[r] not in hashMapS.keys():
                hashMapS[s[r]] = 1
            else:
                hashMapS[s[r]] += 1
            
            if r-l+1 == window:
                if hashMapS == hashMapP:
                    location.append(l)
                hashMapS[s[l]] -= 1
                if hashMapS[s[l]] == 0:
                    hashMapS.pop(s[l])
                l+=1
            r+=1
        print(location)
        return location




        
        