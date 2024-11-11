class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_height_to_left  = [0]*len(height)
        max_height_to_right = [0]*len(height)
        max_height_to_left[0] = height[0]
        max_height_to_right[-1] = height[-1]

        #filling up the max heights to left of each height
        for i in range(1,len(height)):
            max_height_to_left[i] = max(max_height_to_left[i-1],height[i])

        #filling up the max heights to right of each height
        for j in range(len(height)-2,-1,-1):
            max_height_to_right[j] = max(max_height_to_right[j+1],height[j])

        total_trapped_water = 0
        for i in range(len(height)):
            total_trapped_water += min(max_height_to_left[i],max_height_to_right[i]) - height[i]

        return total_trapped_water