class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        l = 0
        r = 0
        count = 0
        vowels = set("aeiou")
        hashMap = {}
        
        for i in range(len(word)):
            if word[i] in vowels:
                l = i
                r = i
                break
        while r < len(word):
            if word[r] in vowels:
                hashMap[word[r]] = r
                if word[l] not in vowels:
                    l = r
            
            while len(hashMap.keys()) > 0 and word[r] not in vowels:
                hashMap = {}
                l = r
                
            
            if len(hashMap.keys()) == 5 and min(hashMap.values()) > -1:
                #print(hashMap)
                count += min(hashMap.values()) - l +1
            r+=1
        print(count)
        return count