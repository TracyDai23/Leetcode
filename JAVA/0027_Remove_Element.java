//这个方法是把所有的不等于val的数一个一个往前面挪。
class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        for (int j = 0; j<nums.length; ++j){
            if (nums[j] != val){
                nums[i] = nums[j];
                ++i;
            }
        }
    // System.out.println(Arrays.toString(nums));
    return i;
    }
}

//第二个方法是减少交换，通过把需要换的换到array最后一个的方法
class Solution {
    public int removeElement(int[] nums, int val) {
        int i = nums.length;
        int j = 0;
        while (j<i){
            if (nums[j] == val){
                nums[j] = nums[i-1];
                --i;   
            } else {
                ++j;
            }
        }
    // System.out.println(Arrays.toString(nums));
    return i;
    }
}
