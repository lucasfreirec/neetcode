class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mySet = set()
        
        for n in nums:
            mySet.add(n)

        minHeap = []

        for n in mySet:
            seq = set()
            if not(n-1 in mySet):
                seq.add(n)
                
                while n+1 in mySet:
                    seq.add(n+1)
                    n +=1
                
                heapq.heappush(minHeap, -len(seq))

        return -minHeap[0]

                    

