class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in range(len(strs)):
            countW = [0] * 26

            for j in range(len(strs[i])):
                countW[ord(strs[i][j]) % 97] = 1 + countW[ord(strs[i][j]) % 97]
            
            
            wordsCounted = tuple(countW)
            
            if wordsCounted not in groups:
                groups[wordsCounted] = []
                
            groups[wordsCounted].append(strs[i])
        
        sublists = []
        for val in groups.values():
            sublists.append(val)

        return sublists


        


        
            
