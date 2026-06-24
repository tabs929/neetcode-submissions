class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def findPali(s,l,r):
            res = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            return res

        for i in range(len(s)):
            res+=findPali(s,i,i)
            res+=findPali(s,i,i+1)
        
        return res