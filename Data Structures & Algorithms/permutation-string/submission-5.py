class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        if s1 == s2:
            return True

        l = sorted(list(s1)) # O(m log m) only the list is O(m)

        print(l)
        window = [n for n in s2[:len(s1)]] # O(m) where m is the len s1
        res = False

        for r in range(1, len(s2)): #O(k) where k is the len of s2
            if (l == sorted(window)): # O (m log m)
                res = True
                break
            else:
                window = [n for n in s2[r:r+len(s1)]]


        return res # time: O (k * m * log m)
                   # space: O (m)
                   # where k = len(s2), m = len(s1)