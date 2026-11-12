class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(i, n):
            if n == 0:
                res.append(path[:])
                return
            if i == len(candidates) or n < 0:
                return
            
            path.append(candidates[i])
            backtrack(i + 1, n - candidates[i])
            path.pop()
            while (i < len(candidates) - 1 and candidates[i] == candidates[i+1]):
                i += 1
            backtrack(i + 1, n)

        backtrack(0, target)

        return res
