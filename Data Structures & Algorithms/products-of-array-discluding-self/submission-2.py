class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_noZero = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                total_noZero = total_noZero * nums[i]

        final = [0] * len(nums)

        for i in range(len(nums)):
            if zero_count > 1:
                break
            elif zero_count == 1:
                if nums[i] == 0:
                    final[i] = total_noZero
                    break
            else:
                final[i] = int(total_noZero / nums[i])
            
        
        return final