class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xfffffff
        while (b&mask) > 0:
            a,b = a^b,(a&b)<<1
        
        return (a&mask) if b>0 else a