class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxVal = 0 
        altitude = 0

        for i in gain:
            altitude += i
            maxVal = max(maxVal, altitude)
        return maxVal