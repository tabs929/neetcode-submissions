class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        stk = []

        for p,s in sorted(pairs)[::-1]:
            stk.append((target - p)/s)
            if len(stk)>=2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)