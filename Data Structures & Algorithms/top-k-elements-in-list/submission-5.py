import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)

        for n in nums:
            numCount[n] += 1
                    
        
        heap = [(-v, k) for k, v in numCount.items()]
        heapq.heapify(heap)
        topK = []
        for _ in range(k):
            topK.append(heap[0][1])
            heapq.heappop(heap)

        return topK


