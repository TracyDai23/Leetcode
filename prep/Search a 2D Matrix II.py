class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]] or matrix ==[]:
            # print('empty matrix')
            return False

        i, j = 0, len(matrix[0])-1
        for i in range(len(matrix)):
            j = len(matrix[0])-1
            if matrix[i][j]<target:
                continue
            else:
                while j >= 0:
                    if matrix[i][j] == target:
                        return True
                    j-=1
        
        return False
