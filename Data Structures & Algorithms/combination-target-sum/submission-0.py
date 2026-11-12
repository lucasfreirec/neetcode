class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i, acc):
            if acc == 0:
                res.append(path[:])
                return        
            if i == len(nums) or acc < 0:
                return

            path.append(nums[i])
            backtrack(i, acc - nums[i])
            path.pop()

            backtrack(i + 1, acc)


        backtrack(0, target)    

        return res
