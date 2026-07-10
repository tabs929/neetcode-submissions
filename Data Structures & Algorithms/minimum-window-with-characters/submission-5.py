class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = defaultdict() ; need = Counter(t)
        have = 0 ; countT = len(need)

        l = 0
        res , minLen = [-1,-1], float("inf")

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in need and need[c] == window[c]:
                have+=1
            
            while have == countT:
                if minLen > r-l+1:
                    res = [l,r]
                    minLen = r - l +1
                
                window[s[l]]-=1
                if s[l] in need and need[s[l]] > window[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if minLen != float("inf") else ""