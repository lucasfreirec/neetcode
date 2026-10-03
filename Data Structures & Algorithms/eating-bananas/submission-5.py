class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMin= 1
        kMax = max(piles)

        while kMin < kMax:
            k = kMin + (kMax - kMin) // 2
            nbHours = 0 

            for i in range(len(piles)):
                nbHours += math.ceil(piles[i] / k)

            if nbHours <= h:
                kMax = k
            else:
                kMin = k + 1
            
        return kMax