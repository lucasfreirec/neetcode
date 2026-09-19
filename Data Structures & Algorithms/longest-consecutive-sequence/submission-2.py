class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mySet = set(nums) # O(n)

        minHeap = []
        maxSeq = 0

        for n in mySet:
            seq = set()
            if n-1 not in mySet:
                length = 1
                
                while n + length in mySet:
                    length += 1
                
                maxSeq = max(maxSeq, length)

        return maxSeq 
                    

