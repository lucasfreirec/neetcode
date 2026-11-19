class Solution:
    def isHappy(self, n: int) -> bool:
        string = str(n)
        res = 0
        visited = set()

        for n in string:
            res += int(n)**2

        while res != 1 and res not in visited:
            visited.add(res)
            resStr = str(res)
            res = 0

            for n in resStr:
                res += int(n)**2

        
        return True if res == 1 else False
