class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hm = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for c in s:
            if c not in hm:
                stk.append(c)
            else:
                if stk and hm[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
    
        return len(stk) == 0