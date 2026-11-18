class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        most_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            most_area = max(most_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return most_area