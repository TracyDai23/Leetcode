class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length <= 2) {
            return res;
        }
        
        Arrays.sort(nums);
        // System.out.println(Arrays.toString(nums));
        for(int i = 0; i<nums.length-2; i++) {
            //deduplicate when sum field is the same, ignore.
            if(i>0 && nums[i-1] == nums[i]) continue;          
            int low = i+1, high = nums.length-1, sum = 0 - nums[i];
            
            while (low < high) {
                // System.out.println("i: "+i +", low: "+low +", high: "+high);
                if (nums[low] + nums[high] == sum) {
                    res.add(Arrays.asList(nums[i], nums[low], nums[high]));
                    while(low< high && nums[low] == nums[low+1]) low++;
                    while(low < high && nums[high] == nums[high-1]) high--;
                    
                    //Incorrect deduplicate solution, because 1) could have multiple element with the same value, so need while loop here; 2) need to check low< high so that it will not out of range.
//                     if (nums[low] == nums[low+1]) low++;
//                     if (nums[high] == nums[high-1]) high--;
                    //After deduplicate, move pointers to next options.
                    low++;
                    high--;
                } else if (nums[low] + nums[high] < sum) low++;
                else high--;

            // System.out.println(res);     
            }
        }
        return res;
    }
} 


// Initial JAVA draft
 public List<List<Integer>> threeSum(int[] nums) {
        // Two Pointer: 
        // 1. sort the array; 2. set three pointers, one is target; the other two pointers are moving pointers
        // 2(c). when two pointer total is higher than target, then move down h pointer, else move up l pointer.
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        while(l < h) {
            int target = -nums[t];
            int l = t+1, h = nums.length-1;
            if(target == nums[l] + nums[h]) {
                res.add(Arrays.asList(nums[t],nums[l++],nums[h--]));
            } else if (target < nums[l] +nums[h]) {
                h--;
            } else {
                l++;
            }
        }
        return res;
    }
}
