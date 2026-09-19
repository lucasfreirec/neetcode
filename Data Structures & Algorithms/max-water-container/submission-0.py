class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i, j = 0, len(heights) - 1
        area = j * min(heights[0], heights[len(heights)-1])

        while i < j:
            minimal = min(heights[i], heights[j])

            if minimal == heights[i]:
                    i += 1
            else:
                    j -= 1
            
            if i < j:     
                area = max(area, (j - i) * min(heights[i], heights[j]))

        return area
            


