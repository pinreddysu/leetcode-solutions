class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.countOfSubStringsWithK(word, k) - self.countOfSubStringsWithK(word, k-1)
    def countOfSubStringsWithK(self, word, k):
        vowels = set("aeiou")
        vowelsCheck = {
            "a": -1,
            "e": -1,
            "i": -1,
            "o": -1,
            "u": -1
        }
        consonantsCount = 0 
        hashMap = {}
        count = 0
        l = 0
        r = 0

        while r < len(word):
            if k < 0:
                return 0
            if word[r] in vowels:
                vowelsCheck[word[r]] = r
            else:
                consonantsCount += 1
            
            while consonantsCount > k:
                if word[l] not in vowels:
                    consonantsCount -= 1
                l+=1
            
            if len(vowelsCheck.keys()) == 5 and min(vowelsCheck.values()) >= l:
                count += min(vowelsCheck.values()) - l + 1

            r+=1
        print(count)
        return count