class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(path[:])
                return

            path.append(nums[i]) # add 
            backtrack(i + 1)
            path.pop() #not add
            
            while i < len(nums) - 1 and nums[i] == nums[i+1]: i += 1

            backtrack(i + 1)
        
        backtrack(0)
        
        return res