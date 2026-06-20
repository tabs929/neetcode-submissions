class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        op = [intervals[0]]

        for s, e in intervals[1:]:
            if s <= op[-1][1]:
                op[-1][1] = max(op[-1][1],e)
            else:
                op.append([s,e])

        return op