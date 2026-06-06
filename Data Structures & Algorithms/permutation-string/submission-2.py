from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # k = len(s1)
        # seen = Counter()
        # need = Counter(s1)
        # left = 0

        # for right in range(len(s2)):
        #     seen[s2[right]] += 1

        #     if right >= k:
        #         left_c = s2[right - k]
        #         seen[left_c]-=1
                
        #         if seen[left_c] == 0:
        #             del seen[left_c]

        #     if seen == need:
        #         return True

        # return False

        left = 0
        seen = Counter()
        want = Counter(s1)

        for right in range(len(s2)):
            seen[s2[right]]+=1

            while seen > want :
                seen[s2[left]]-=1
                left+=1
                if seen[s2[left]] == 0:
                    del seen[s2[left]]

            if seen == want:
                return True
        return False

