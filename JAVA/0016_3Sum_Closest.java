// Self resolved based on 0015. 
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length <= 2) {
            return 0;
        }
        //
        Arrays.sort(nums);
        int diff = Integer.MAX_VALUE;
        for(int i = 0; i<nums.length -2; i++) {
            if(i> 0 && nums[i-1] == nums[i]) continue;
            int low = i+1, high = nums.length -1, sum = target -nums[i];
            
            while(low < high) {
                
                if (Math.abs(nums[low] + nums[high] - sum) <Math.abs(diff)){
                        diff = nums[low] + nums[high] - sum;
                    }
                if(nums[low] + nums[high] - sum >0) {
                    high--;
                } else if (nums[low] + nums[high] - sum <0){
                    low++;
                } else {
                    System.out.println("Landed here.");
                    return target;
                }
                // System.out.println("i: "+i +", low: "+low +", high: "+high+", sum: "+sum+", diff: "+diff);
            }
        }
        return diff+target;
    }
}
