class Solution {
    public int minEatingSpeed(int[] piles, int H) {
        int l = 1, r = 1_000_000_000; // r cannot be Integer.MAX_VALUE, which will trigger Runtime Error.
        while(l<r) {
            int mid = (l+r)/2;
            if (!calculateTaken(piles, H, mid)) {
                l = mid + 1;
            } else {
                r = mid; // why we cannot "-1" on this step like general Binary search solution?
            }
        }
        return l;
        
    }
    // Can Koko eat all bananas in H hours with eating speed K?
    private boolean calculateTaken (int[] piles, int H, int mid) {
        int taken = 0;
        for (int pile: piles) {
            taken += (pile -1) / mid + 1; //why need to pile -1
        }
        return taken <= H;
    }
}


// My initial attempt wrong answer, did not resolve corner case:
class Solution {
    public int minEatingSpeed(int[] piles, int H) {
        int l = 0, r = Integer.MAX_VALUE, mid =(l+r)/2;
        int taken = 0;
        while(l<r) {
            mid = (l+r)/2;
            taken = calculateTaken(piles, mid);
            if (taken ==H && l == mid) {
                return l;
            } else if (taken > H) {
                l = mid + 1;
            } else if (taken < H){
                r = mid -1;
            } else {
                r -=1;
            }
        }
        return 0;
        
    }
    
    private int calculateTaken (int[] piles, int mid) {
        int taken = 0;
        for (int pile: piles) {
            taken += (int) Math.ceil((double)pile / mid);
        }
        return taken;
    }
}
