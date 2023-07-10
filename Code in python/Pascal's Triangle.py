class Solution(object):
    

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(2, numRows+1):
            l = [1] * (i)
            for j in range(1,i-1):
                l[j] = res[i-2][j] + res[i-2][j-1]
            res.append(l)

        return res
