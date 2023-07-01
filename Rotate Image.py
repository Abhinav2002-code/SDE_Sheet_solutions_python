class Solution(object):
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
                

        for i in range(row):
            matrix[i].reverse()
        return matrix

