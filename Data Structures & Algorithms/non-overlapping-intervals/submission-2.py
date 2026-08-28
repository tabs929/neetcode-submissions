class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x:x[0])
        ini_end = intervals[0][1]

        for start,end in intervals[1:]:
            if start >= ini_end:
                ini_end = end
            else:
                res+=1
                ini_end = min(end,ini_end)
        return res