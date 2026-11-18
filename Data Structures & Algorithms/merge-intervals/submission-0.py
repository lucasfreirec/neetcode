class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals)
        res = [sortedIntervals[0][:]]

        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] <= res[-1][1]:
                if sortedIntervals[i][1] > res[-1][1]:
                    res[-1][1] = sortedIntervals[i][1]
            else:
                res.append(sortedIntervals[i])

        return res