class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
                
        while i < j:
            while numbers[j] + numbers[i] < target and i < j:
                i += 1
            while numbers[j] + numbers[i] > target and i < j:
                j -= 1

            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]