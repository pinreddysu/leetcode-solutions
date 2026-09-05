class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLen = len(s1)
        l = 0
        r = 0
        hashSet1 = {}
        for i in s1:
            if i not in hashSet1.keys():
                hashSet1[i] = 1
            else:
                hashSet1[i] += 1
        hashMap = {}

        while r< len(s2):
            if s2[r] not in hashMap.keys():
                hashMap[s2[r]] = 1
            else:
                hashMap[s2[r]] += 1
            
            if r-l+1 == windowLen:
                if hashMap == hashSet1:
                    return True
                
                hashMap[s2[l]] -= 1
                if hashMap[s2[l]] == 0:
                    hashMap.pop(s2[l])
                l+=1
            r+=1
        return False
                


        