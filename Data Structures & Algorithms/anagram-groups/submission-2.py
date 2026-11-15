class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            countWord = [0] * 26

            for c in s:
                countWord[ord(c) - ord("a")] += 1
            
            res[tuple(countWord)].append(s)

        return list(res.values())
                
        
            