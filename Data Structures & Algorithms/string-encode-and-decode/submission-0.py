class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for word in strs:
            encodedStr += str(len(word)) + '#' + word

        return encodedStr
            

    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0

        while i < len(s):
            decodedLen = ''

            while s[i] != '#':
                decodedLen += s[i]
                i += 1

            i += 1

            length = int(decodedLen)

            decodedWord = ''

            for j in range(length):
                decodedWord += s[i]
                i += 1

            decodedList.append(decodedWord)

        return decodedList



