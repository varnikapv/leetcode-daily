class Solution {
    public static int houseRobber(int[] nums, int i){
       
       //base condition
        if  ( i >= nums.length){
            return 0;
        }
        //logic
        int include = nums[i] + houseRobber(nums, i+2);
        int exclude = houseRobber(nums, i+ 1);

        return Math.max(include, exclude);
    
    }

    public int rob(int[] nums) {
        return houseRobber(nums, 0);
    }
}