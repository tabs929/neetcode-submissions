class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda i : i[0])
        initEnd = intervals[0][1]
        
        for s,e in intervals[1:]:
            if s >= initEnd:
                initEnd = e
            else:
                count+=1
                initEnd = min(e, initEnd)
        return count