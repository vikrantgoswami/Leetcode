public class TotalTrappedWater {
    public int trap(int[] height) {
        if (height.length == 0) {
            return 0;
        }
        int n = height.length;
        int[] maxHeightToLeft = new int[n];
        int[] maxHeightToRight = new int[n];
        int totalTrappedWater = 0;
        maxHeightToLeft[0] = height[0]; // since there is no height to left of first element
        maxHeightToRight[n - 1] = height[n - 1]; // since there is no height to right of last element

        // now we find the max heights to left of each height
        for (int i = 1; i < n; i++) {
            maxHeightToLeft[i] = Math.max(maxHeightToLeft[i - 1], height[i]);
        }

        // now we find the max heights to right of each height
        for (int i = n - 2; i >= 0; i--) {
            maxHeightToRight[i] = Math.max(maxHeightToRight[i + 1], height[i]);
        }

        // now we calculate the total trapped water
        for (int i = 0; i < n; i++) {
            totalTrappedWater += Math.min(maxHeightToRight[i], maxHeightToLeft[i]) - height[i];
        }

        return totalTrappedWater;
    }
}
