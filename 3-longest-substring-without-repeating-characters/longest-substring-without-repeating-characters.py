class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return self.optimizedSolution(s)
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
    #if we use string the TC is o^2 because for subString[1:] there's a loop running to copy it so use set that way O(n) and o(1)
    def betterSolution(self, s):
        l, r, subStringSet = 0, 0, set()
        maxLength = 0

        while r < len(s):
            
            while s[r] in subStringSet:
                subStringSet.remove(s[l])
                l+=1
            else:
                subStringSet.add(s[r])
                maxLength = max(maxLength, r-l+1)

            r += 1
        return maxLength

    #Optimized solution: since the solution does not care about substring only the length
    




        