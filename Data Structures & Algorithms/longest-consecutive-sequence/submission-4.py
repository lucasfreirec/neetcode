class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums) # O(n)
        res = 0

        for n in mySet:
            if n-1 not in mySet:
                length = 1
                
                while n + length in mySet:
                    length += 1
                
                res = max(res, length)

        return res