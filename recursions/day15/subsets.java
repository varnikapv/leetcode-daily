package recursions.day15;

import java.util.ArrayList;
import java.util.List;

public class subsets {
    class Solution {
    public void helper(int index, int[] nums, List<Integer> list1,
     List<List<Integer>> ans){

        ans.add(new ArrayList<>(list1));
        // exploring the elements
        for(int i = index; i < nums.length; i++){
            list1.add(nums[i]);
        helper(i+1, nums,list1,ans);
        //backTracking
        list1.remove(list1.size() - 1);
        }
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        helper(0,nums,new ArrayList<>(),ans);
        return ans;
     
    }
}
}
