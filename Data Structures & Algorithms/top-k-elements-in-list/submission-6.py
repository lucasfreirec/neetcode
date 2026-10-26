class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        freqSorted = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        res = []

        for i in range(k):
            res.append(freqSorted[i][0])
        
        return res
