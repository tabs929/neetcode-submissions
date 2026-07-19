class Solution:
    def isHappy(self, n: int) -> bool:
        t = 0
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumofsquares(n)
            if n == 1:
                return True
        return False                    
    
        return False
    def sumofsquares(self,n):
        t = 0
        while n:
            units_place = n%10
            t += units_place**2
            n = n//10
        return t