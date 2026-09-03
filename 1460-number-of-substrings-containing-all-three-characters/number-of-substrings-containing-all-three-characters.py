class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return self.betterSolution(s)
    
    def bruteForceSolution(self,s):
        totalSubStrings = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i, len(s)):
                hashSet.add(s[j])
                if len(hashSet) == 3:
                    totalSubStrings += 1
        print(totalSubStrings)
        return totalSubStrings
    
    def bruteForceSolutionOptimized(self, s):
        totalSubStrings = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i, len(s)):
                hashSet.add(s[j])
                if len(hashSet) == 3:
                    totalSubStrings += len(s) - j
                    break
        print(totalSubStrings)
        return totalSubStrings
    
    def betterSolution(self, s):
        totalSubStrings = 0
        l = 0
        r = 0
        hashMap = {}
        while r < len(s):
            if s[r] not in hashMap.keys():
                hashMap[s[r]] = 1
            else:
                hashMap[s[r]] += 1
            
            if len(hashMap.keys()) == 3:
                totalSubStrings += len(s) - r
            
            while len(hashMap.keys()) == 3:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    hashMap.pop(s[l])
                if len(hashMap.keys()) == 3:
                    totalSubStrings += len(s) - r
                l+=1
            
            if len(hashMap.keys()) < 3:
                r+=1
        print(totalSubStrings)
        return totalSubStrings


       