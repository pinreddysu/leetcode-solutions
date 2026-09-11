class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        r = 0
        hashMap = {}
        minLen = math.inf
        startInd = -1
        count = 0

        while r < len(cards):
            
            if cards[r] in hashMap.keys():
                print(cards[r])
                minLen = min(minLen, r - hashMap[cards[r]]+1)
                hashMap[cards[r]] = r
            if cards[r] not in hashMap.keys():
                hashMap[cards[r]] = r
            r+=1
        print(minLen)
        if minLen == math.inf:
            return -1
        return minLen
