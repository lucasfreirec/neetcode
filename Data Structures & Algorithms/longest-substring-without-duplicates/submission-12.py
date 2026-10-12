class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in sub:
                res = max(res, len(sub))

                while l < r and s[r] in sub:
                    sub.remove(s[l])
                    l += 1
            
            sub.add(s[r])
            res = max(res, len(sub))

        return res
