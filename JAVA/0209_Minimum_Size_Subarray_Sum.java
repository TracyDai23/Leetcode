// Follow up question requires O(nlogn) which uses Binary Search. 
// I did not figured it out but read solution: O(NLogN) - search if a window of size k exists that satisfy the condition
public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int i = 1, j = nums.length, min = 0;
        while (i <= j) {
            int mid = (i + j) / 2;
            if (windowExist(mid, nums, s)) {
                j = mid - 1;
                min = mid;
            } else i = mid + 1;
        }
        return min;
    }


    private boolean windowExist(int size, int[] nums, int s) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i >= size) sum -= nums[i - size];
            sum += nums[i];
            if (sum >= s) return true;
        }
        return false;
    }
}

// My answer:  O(n): Two Pointer
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (Arrays.stream(nums).sum()< s) return 0;
        
        int l = 0, r = 0, res= Integer.MAX_VALUE;
        while (l<= r && r < nums.length){
            if (sum(l,r,nums) < s) {
                r +=1;
            } else if (sum(l,r,nums) >= s) {
                res = Math.min((r-l)+1,res);
                l +=1;
            }
        }
        return res;
    }
    
    private int sum(int l, int r, int[] nums) {
        int res = 0;
        for (int i = l; i <= r; i++) {
            res += nums[i];
        }
        return res;
    }
}
