class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1

        while t <= b:
            midRow = t + (b - t) // 2

            if target >= matrix[midRow][0] and target <= matrix[midRow][len(matrix[0]) - 1]:
                while l <= r:
                    midCol = l + (r - l) // 2

                    if target == matrix[midRow][midCol]:
                        return True
                    elif target > matrix[midRow][midCol]:
                        l = midCol + 1
                    else:
                        r = midCol - 1
                return False
            elif target < matrix[midRow][0]:
                b = midRow - 1
            else:
                t = midRow + 1
        
        return False

                
            