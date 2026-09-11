class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lPoints = sum(cardPoints[:k])
        rPoints = 0
        totalPoints = lPoints + rPoints
        maxPoints = totalPoints
        l = k-1
        r = len(cardPoints) -1
        
        while r > len(cardPoints) - k - 1:
            lPoints -= cardPoints[l]
            l -= 1
            rPoints += cardPoints[r]
            r -= 1
            totalPoints = lPoints + rPoints
            maxPoints = max(maxPoints, totalPoints)
        print(maxPoints)
        return maxPoints