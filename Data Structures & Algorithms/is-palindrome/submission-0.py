class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isValid(c: str) -> bool:
            if 'a' <= c <= 'z':
                return True
            if 'A' <= c <= 'Z':
                return True
            if '0' <= c <= '9':
                return True

            return False

        i = 0
        j = len(s) - 1

        while i < j:

            while i < j and not isValid(s[i]):
                i += 1

            while i < j and not isValid(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True # time: O(n), space: O(n), where n is the length of the string
