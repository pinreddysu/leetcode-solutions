class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        What is my window?
        -> My window is variable as we are finding largest substring with unique
        characters meaning finding largest window where all of them are unique
        What makes it invalid?
        -> Finding a repeated character
        When do I move right?
        -> I move right when there is unique character
        When do I move left?
        -> I move left until I remove the duplicate character
        What does my hashmap/count store?
        -> I store the frequency because to know how many times a character
        has repeated
        Am I finding one window or counting multiple?
        -> Finding the longest window which has distinct characters
        '''
        # return self.bruteForceSolution(s)
        return self.betterSolution(s)

    def bruteForceSolution(self, s):
        maxLen = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i, len(s)):
                if s[j] not in hashSet:
                    hashSet.add(s[j])
                    maxLen = max(maxLen, j-i+1)
                else:
                    break

        print(maxLen)
        return maxLen
    
    def betterSolution(self, s):
        hashMap = {}
        maxLen = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] not in hashMap.keys():
                hashMap[s[r]] = 1
            else:
                hashMap[s[r]] += 1

            while max(hashMap.values()) > 1:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    hashMap.pop(s[l])
                l+=1
            
            if max(hashMap.values()) <= 1:
                maxLen = max(maxLen, r-l+1)
            r+=1
        return maxLen
