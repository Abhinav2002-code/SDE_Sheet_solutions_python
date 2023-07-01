class Solution(object):
    def uniquePaths(self, m, n):
        def fact(n):
            if n < 0:
                raise ValueError("Factorial is undefined for negative numbers.")
            elif n == 0 or n == 1:
                return 1
            else:
                result = 1
                for i in range(2, n + 1):
                    result *= i
            return result
        N = m + n - 2
        r = m - 1
        res = fact(N)/((fact(N-r)) * (fact(r)))
        return res
