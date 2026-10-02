class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minK = 1
        maxK = max(piles)

        while minK < maxK:
            k = minK + (maxK - minK) // 2
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)

            if hours <= h:
                maxK = k
            else:
                minK = k + 1
        
        return minK


