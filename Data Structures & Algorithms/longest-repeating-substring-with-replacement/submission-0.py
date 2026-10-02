class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myTable = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            windowLen = r - l + 1

            myTable[s[r]] += 1

            maxV = max(myTable.values())


            while windowLen - maxV > k:
                myTable[s[l]] -= 1
                l += 1
                maxV = max(myTable.values())
                windowLen -= 1
            
            res = max(res, windowLen)

        return res
