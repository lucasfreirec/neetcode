class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_arr = [0] * len(nums)
        suf_arr = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            if i == 1:
                pre_arr[i] = nums[i-1]
                continue
            pre_arr[i] = pre_arr[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            if i == len(nums)-2:
                suf_arr[i] = nums[i+1]
                continue
            suf_arr[i] = suf_arr[i+1] * nums[i+1]

        final = [0] * len(pre_arr)

        for i in range(len(final)):
            if i == 0 or i == len(final)-1:
                final[i] = pre_arr[i] + suf_arr[i]
                continue
            final[i] = pre_arr[i] * suf_arr[i]
        return final