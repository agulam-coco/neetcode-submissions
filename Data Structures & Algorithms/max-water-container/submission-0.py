class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # two pointers on each end start and end
        # calculate the max water with (end-start)*min(height[start], height[end])
        # move only the smaller bar beecause that determines the max

        start_ptr = 0
        end_ptr = len(heights) - 1
        max_height = 0

        while start_ptr < end_ptr:
            curr_height = (end_ptr - start_ptr) * min(heights[start_ptr], heights[end_ptr])
            max_height = max(max_height, curr_height)

            #move smaller bar
            if heights[start_ptr] < heights[end_ptr]:
                start_ptr += 1
            else:
                end_ptr -= 1
        
        return max_height