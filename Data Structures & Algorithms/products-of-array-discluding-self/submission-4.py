class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_arr = [0] * len(nums)
        suf_arr = [0] * len(nums)
        pre_arr[0] = 1
        suf_arr[len(suf_arr)-1]=1

        for i in range(1,len(nums)):
            pre_arr[i] = pre_arr[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suf_arr[i] = suf_arr[i+1] * nums[i+1]

        final = [0] * len(pre_arr)

        for i in range(len(final)):
            final[i] = pre_arr[i] * suf_arr[i]
        return final