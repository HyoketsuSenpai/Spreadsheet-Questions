class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        ans = 0
        for i in range(len(points) - 1):
            ans = max(ans, abs(points[i][0] - points[i + 1][0]))
        
        

        return ans
