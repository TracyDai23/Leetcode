class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        int l = 1, h = x, mid = (l+h)/2;
        while (true) {
            mid = (l+h)/2;
            if(mid >x/mid) {//此处用（mid）*（mid）>x 会overflow，因为java对int的最大值的界限的原因？ e.g. x = 2147395599
                h = mid-1;
            } else {
                if ((mid+1) >x/(mid+1)) { //此处用（mid+1）*（mid+1）>x 会overflow
                    return mid;
                }
                l = mid+1;
            }
        }
    }
}
