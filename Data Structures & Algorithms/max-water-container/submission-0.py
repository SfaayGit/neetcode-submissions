class Solution:
    def maxArea(self, heights: List[int]) -> int:
       left, right = 0, len(heights)-1
       area = 0
       while left < right:
           if (heights[left] < heights[right]):
               currarea = min(heights[left],heights[right]) * (right - left)
               area = max(area, currarea)
               left +=1
           else:
                currarea = min(heights[left],heights[right]) * (right - left)
                area = max(area, currarea)
                right -= 1 
       return area