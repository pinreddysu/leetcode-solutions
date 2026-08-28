class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Brute force: generating all the subarrays that unique
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

        