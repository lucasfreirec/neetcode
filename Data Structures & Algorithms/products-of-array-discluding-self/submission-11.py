class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_array = [0] * len(nums)
        suff_array = [0] * len(nums)
        pref_array[0] = 1
        suff_array[len(suff_array) - 1] = 1

        for i in range(1, len(pref_array)):
            pref_array[i] = pref_array[i-1] * nums[i-1]
        
        for i in range(len(suff_array) - 2, -1, -1):
            suff_array[i] = suff_array[i+1] * nums[i+1]
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = suff_array[i] * pref_array[i]

        return res

