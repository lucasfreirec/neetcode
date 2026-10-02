class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        if s1 == s2:
            return True

        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        l = 0

        for c in s1:
            counter1[c] += 1
        

        
        for r in range(len(s2)):
            counter2[s2[r]] += 1
            
            if r - l + 1 == len(s1):
                if counter1 == counter2:
                    return True
                
                counter2[s2[l]] -= 1
                if counter2[s2[l]] == 0:
                    del counter2[s2[l]]
                    
                l += 1

        return False