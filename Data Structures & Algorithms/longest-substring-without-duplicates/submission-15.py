class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in subString:
                res = max(res, len(subString))

                while s[r] in subString:
                    subString.remove(s[l])
                    l += 1

            subString.add(s[r])
            res = max(res, len(subString))
        
        return res
