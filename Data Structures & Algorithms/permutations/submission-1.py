#optimization with set()

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for n in nums: # O(n)
                if n in used: # O(1)
                    continue

                path.append(n)
                used.add(n)
                backtrack()
                path.pop()
                used.remove(n)

        backtrack()
        return res
        #time complexity: O(n * n!)
        #space complexity: O(n)
        #where n = len(nums)