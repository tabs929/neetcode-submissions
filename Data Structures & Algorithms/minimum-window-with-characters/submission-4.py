from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""

        want = Counter(t)
        count = defaultdict(int)

        have, need = 0,len(want)
        res, min_len = [-1,-1], float("inf")

        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1

            if s[r] in want and count[s[r]] == want[s[r]]:
                have+=1

            while have == need :
                if (r - l + 1) < min_len:
                    res = [l,r]
                    min_len = r - l + 1
                count[s[l]] -=1
                if s[l] in want and count[s[l]] < want[s[l]]:
                    have-=1
                l+=1

        l,r = res
        return s[l:r+1] if min_len != float("inf") else ""