class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        minRate = r

        while l<=r:
            m = (l+r)//2
            hrs = 0
            for p in piles:
                hrs+= math.ceil(p/m)
            
            if hrs > h:
                l = m+1
            else:
                minRate = m
                r = m-1
        return minRate