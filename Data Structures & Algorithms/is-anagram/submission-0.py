class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        
        if Counter(s) == Counter(t):
            return True

        return False