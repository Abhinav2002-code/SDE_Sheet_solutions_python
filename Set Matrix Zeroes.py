class Solution(object):
    def setZeroes(self, matrix):

        row = [0] * len(matrix)
        col = [0] * len(matrix[0])

        for i in range(len(row)):
            for j in range(len(col)):
                if (matrix[i][j] == 0):
                    row[i] = 1
                    col[j] = 1
        for i in range(len(row)):
            for j in range(len(col)):
                if(row[i] or col[j]):
                    matrix[i][j] = 0


        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
