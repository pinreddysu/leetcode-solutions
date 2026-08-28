class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.betterSolution(s)
        # return self.bruteForceSolution(s)
    #Brute force: generating all the subarrays that unique
    def bruteForceSolution(self, s):
        maxLength = 0
        for i in range(len(s)):
            subString = ""
            for j in range(i,len(s)):
                if not s[j] in subString:
                    subString += s[j]
                    maxLength = max(len(subString), maxLength)
                elif s[j] in subString:
                    break
        return maxLength
    
    #Better Solution: expand when condition is met and shrink when its not
    def betterSolution(self, s):
        l, r, subString = 0, 0, ""
        maxLength = 0

        while r < len(s):
            
            # print(subString)
            while s[r] in subString:
                subString = subString[1:]
                l+=1
            else:
                subString+=s[r]
                maxLength = max(maxLength, r-l+1)

            r += 1
        return maxLength


        