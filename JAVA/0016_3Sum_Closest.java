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
                if (nums[low] + nums[high] - sum <diff){
                        diff = nums[low] + nums[high] - sum;
                        while (low < high && nums[low] == nums[low+1]) low++;
                        while (low < high && nums[high] == nums[high-1]) high--;
                    }
                if(nums[low] + nums[high] - sum >0) {
                    high--;
                } else if (nums[low] + nums[high] - sum <0){
                    low++;
                } else {
                    return target;
                }
                    
            }
        }
        return diff+target;
    }
}
