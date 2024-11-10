public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        // 2-pointer approach
        int maxWater = 0;
        int l = 0;
        int r = height.length - 1;
        while (l < r) {
            maxWater = Math.max(((r - l) * Math.min(height[l], height[r])), maxWater);
            if (height[l] > height[r]) {
                r--;
            } else {
                l++;
            }

        }
        return maxWater;
    }
}
