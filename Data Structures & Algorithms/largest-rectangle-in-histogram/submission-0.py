class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[-1]
        area=0
        for i in range(len(heights)):
            while stack[-1]!=-1 and heights[stack[-1]]>=heights[i]:
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                area=max(area,h*w)
            stack.append(i)
        
        while stack[-1]!=-1:
            h=heights[stack.pop()]
            w=len(heights)-stack[-1]-1
            area=max(area,h*w)
        return area
