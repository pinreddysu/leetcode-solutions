class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        l = 0
        r = 9
        hashMap = {}
        subStrings = []

        while r < len(s):
            if s[l:r+1] not in hashMap.keys():
                hashMap[s[l:r+1]] = 1
            else: 
                hashMap[s[l:r+1]] +=1
        
            if hashMap[s[l:r+1]] > 1:
                if s[l:r+1] not in subStrings:
                    subStrings.append(s[l:r+1])
            l+=1
            r+=1
 
        return subStrings
        
        
        
        