class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        return self.betterSolution(fruits)
        
    def bruteForceSolution(self, fruits):
        maxLen = 0
        for i in range(len(fruits)):
            hashSet = set()
            for j in range(i, len(fruits)):
                if fruits[j] not in hashSet:
                    hashSet.add(fruits[j])
                if len(hashSet) > 2:
                    break
                else:
                    maxLen = max(maxLen, j-i+1)
        print(maxLen)
        return maxLen
    
    def betterSolution(self, fruits):
        l = 0
        r = 0
        maxLen = 0
        fruitsTaken = {}

        while r < len(fruits):
            if fruits[r] not in fruitsTaken.keys():
                fruitsTaken[fruits[r]] = 1
            else:
                fruitsTaken[fruits[r]] +=1
            
            while len(fruitsTaken.keys()) > 2:
                fruitsTaken[fruits[l]] -= 1
                if fruitsTaken[fruits[l]] == 0:
                    fruitsTaken.pop(fruits[l])
                l+=1
            
            if len(fruitsTaken.keys()) <= 2:
                maxLen = max(maxLen, r-l+1)
                r+=1
        return maxLen
        