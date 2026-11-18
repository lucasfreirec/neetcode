class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-n for n in stones]
        heapq.heapify(weights)

        while weights:
            if len(weights) == 1:
                return -weights[0]
            
            x = -heapq.heappop(weights)
            y = -heapq.heappop(weights)
            diff = abs(x - y)
            if diff > 0:
                heapq.heappush(weights, -diff)
        return 0