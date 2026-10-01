class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            if s[r] in mySet:
                while s[r] in mySet:
                    mySet.remove(s[l])
                    l += 1
            
            mySet.add(s[r])
            maxLen = max(maxLen, r - l + 1)   
                    
        return maxLen #time: O(n), space: O(m) where m is the number of substring without duplicates

