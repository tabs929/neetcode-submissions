from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = Counter()
        need = Counter(s1)
        left = 0

        for right in range(len(s2)):
            seen[s2[right]] += 1

            while seen > need:
                seen[s2[left]]-=1
                left+=1
                if seen[s2[left]] == 0:
                    del seen[s2[left]]

            if seen == need:
                return True

        return False