public class ProdOfArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        //brute force approach
        int[] res = new int[nums.length];
        //Arrays.fill(res, 1); // Set all elements of res to 1

        //prefix & suffix products
        //first we get the products of all prefix to an element
        res[0] = 1; //since no element to right of first element
        for(int i=1; i<nums.length; i++){
            res[i] = res[i-1]*nums[i-1];
        }
        //now we get the product of suffixes for each element
        int suffixProduct = nums[nums.length-1];
        for(int i=nums.length-2; i>=0; i--) {
            res[i] = res[i]*suffixProduct;
            suffixProduct *= nums[i];
        }

        return res;
    }
}{

}
