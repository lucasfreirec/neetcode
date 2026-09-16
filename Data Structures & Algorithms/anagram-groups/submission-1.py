class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for i in strs:
            countW = [0] * 26

            for j in i:
                countW[ord(j) % 97] += 1
            
                
            groups[tuple(countW)].append(i)
        
        return list(groups.values()) #O(m * n)

        
        


        
            
