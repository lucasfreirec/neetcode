class Solution:
    def isHappy(self, n: int) -> bool:
        string = str(n)
        res = 0
        visited = set()

        for d in string:
            res += int(d)**2

        while res != 1 and res not in visited:
            visited.add(res)
            resStr = str(res)
            res = 0

            for d in resStr:
                res += int(d)**2

        
        return True if res == 1 else False
