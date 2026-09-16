class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            x = target - n

            if x in prevMap:
                return [prevMap[x], i]
            
            prevMap[n] = i
