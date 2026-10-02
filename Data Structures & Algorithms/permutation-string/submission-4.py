class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        if s1 == s2:
            return True
        l = sorted(list(s1))
        print(l)
        window = [n for n in s2[:len(s1)]]
        res = False

        for r in range(1, len(s2)):
            if (l == sorted(window)):
                res = True
                break
            else:
                window = [n for n in s2[r:r+len(s1)]]


        return res