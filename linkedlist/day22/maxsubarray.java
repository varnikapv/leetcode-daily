package linkedlist.day22;

public class maxsubarray {
    class Solution {
    public int maxSubArray(int[] nums) {
        int curr_sum = 0;
        int maxsum = Integer.MIN_VALUE;

        for (int i=0; i< nums.length; i++){
             curr_sum = Math.max(nums[i], curr_sum + nums[i]);
            maxsum = Math.max(curr_sum, maxsum);
        }
        
        return maxsum;
    }
}
}
