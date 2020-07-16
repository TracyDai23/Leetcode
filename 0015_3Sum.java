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
