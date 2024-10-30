class Solution {
    public boolean containsDuplicate(int[] nums) {
        //Given an integer array nums, return true if any value appears at least twice in the array, 
        //and return false if every element is distinct.
        Map<Integer,Integer> numsCountMap = new HashMap<Integer,Integer>();
        for(int i=0; i < nums.length; i++){
            if(numsCountMap.containsKey(nums[i])){
                return true;
            }
            else{
                numsCountMap.put(nums[i],1);
            }
        }
        return false;
    }
}