class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)

        while minK < maxK:
            k = minK + (maxK - minK) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours > h:
                minK = k + 1
            else:
                maxK = k
        
        return maxK
            

