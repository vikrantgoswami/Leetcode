class Solution {
    //Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mapOfIndexWithElement = new HashMap<Integer, Integer>();
        int comp;
        for(int i=0; i<nums.length; i++){
            comp = target - nums[i];
            if(mapOfIndexWithElement.keySet().contains(comp)){
                return new int[]{i, mapOfIndexWithElement.get(comp)};
            }
            else{
                mapOfIndexWithElement.put(nums[i],i);
            }
        }
        return null;
    }
}