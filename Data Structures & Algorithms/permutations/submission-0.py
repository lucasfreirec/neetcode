class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for n in nums:
                if n in path:
                    continue
                    
                path.append(n)
                backtrack()
                path.pop()

        backtrack()
        return res