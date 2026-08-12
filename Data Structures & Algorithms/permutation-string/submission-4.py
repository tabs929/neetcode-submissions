class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = Counter()
        want = Counter(s1)
        l = 0

        for r in range(len(s2)):
            seen[s2[r]] = seen.get(s2[r],0) + 1

            while want < seen:
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l+=1
            
            if seen == want:
                return True
        
        return False