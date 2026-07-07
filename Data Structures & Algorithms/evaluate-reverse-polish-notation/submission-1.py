class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:

            if t == "+":
                stk.append(stk.pop()+stk.pop())
            elif t == "*":
                stk.append(stk.pop()*stk.pop())
            elif t == "-":
                a,b = stk.pop() , stk.pop()
                stk.append(b - a)
            elif t == "/":
                a,b = stk.pop() , stk.pop()
                stk.append(int(b / a))
            else:
                stk.append(int(t))
        
        return stk[0]