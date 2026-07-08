class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                ind , height = stk.pop()
                maxArea = max(maxArea , height * (i - ind))
                start = ind
            stk.append((start,h))
        
        for i,h in stk:
            maxArea = max(maxArea, h *(len(heights) - i))
        
        return maxArea