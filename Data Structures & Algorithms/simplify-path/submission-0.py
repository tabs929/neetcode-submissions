class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stk = []

        for d in lst:
            if d == "..":
                if stk:
                    stk.pop()
            elif d != "." and d != "":
                stk.append(d)
        return "/" + "/".join(stk)