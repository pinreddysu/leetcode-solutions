class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        What is my window?
        -> It is variable window which consist of all three characters atleast once
        What makes it invalid?
        -> when there is a missing occurrences of a character
        When do I move right?
        -> To find occurences of all three letters
        When do I move left?
        -> We move left when we found another occurence of the character that we already found
        What does my hashmap/count store?
        -> we will use hashArray to store position of last occurrences to count 
        substrings
        Am I finding one window or counting multiple?
        -> we are counting mutiple windows
        '''
        # return self.bruteForceSolution(s)
        return self.betterSolution(s)

    def bruteForceSolution(self, s):
        count = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i, len(s)):
                hashSet.add(s[j])
                if len(hashSet) == 3:
                    count+=1
        return count
    
    def betterSolution(self, s):
        l = 0
        r = 0
        hashArr = [-1] * 3
        count = 0

        while r < len(s):
            hashArr[ord(s[r]) - ord('a')] = r

            if min(hashArr) > -1:
                count+= min(hashArr) -l +1
            r+=1
        return count

