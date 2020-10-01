class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length < 1 || matrix[0].length < 1) return false;
        int l = matrix[0].length-1, r = 0;
        // System.out.println(r);
        while ((l>=0) && (r<= matrix.length-1)) {
            if (matrix[r][l] == target) {
                return true;
            } else if (matrix[r][l] < target) {
                r +=1;
            } else if (matrix[r][l] > target) {
                l -=1;
            }
        }
        return false;
    }
}
