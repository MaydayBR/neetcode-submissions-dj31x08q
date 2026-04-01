class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(index1, index2):
            length = min(heights[index1],heights[index2])
            width = index2-index1
            return length*width

        l,r = 0,len(heights)-1
        max_area = float("-inf")
        while l < r:
            curr_area = area(l,r)
            max_area = max(max_area,curr_area)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return max_area