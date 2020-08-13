// Typed from solution.
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        return kSum(nums, target, 0,4);
    }
    
    public List<List<Integer>> kSum(int[] nums, int target, int start, int k) {
        List<List<Integer>> res = new ArrayList<>();
        //Filter out three corner cases cuz nums is already sorted:
        // 1. if start point is the end of the nums array;
        // 2. if the value of nums at start times k is already larger than target, meaning all possible sum options will be larger than target. Can return res in this case
        // 3. if the value of nums at then end of the nums array times k is already less than target, meaning all possible sum options will be less than target. Can return res in this case
        if (start == nums.length || nums[start] * k > target || target > nums[nums.length-1] * k)
            return res;
        if (k == 2)
            return twoSum(nums, target, start);
        for (int i = start; i<nums.length; ++i) {
            if(i == start || nums[i-1]!= nums[i]){
                for (var set: kSum(nums, target - nums[i], i+1, k-1)) { // do not understand the var set part
                    res.add(new ArrayList<>(Arrays.asList(nums[i])));
                    res.get(res.size() -1).addAll(set);
                }
            }
        }
        return res;
    }
    
    public List<List<Integer>> twoSum(int[] nums, int target, int start) {
        List<List<Integer>> res = new ArrayList<>();
        int lo = start, hi = nums.length -1;
        while (lo < hi) {
            int sum = nums[lo] + nums[hi];
            if (sum < target || (lo > start && nums[lo] == nums[lo-1]))
                ++lo;
            else if (sum > target || (hi < nums.length -1 && nums[hi] == nums[hi + 1])) 
                --hi;
            else res.add(Arrays.asList(nums[lo++], nums[hi--]));
            
        }
        return res;
    }
}
