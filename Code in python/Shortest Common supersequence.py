from os import *
from sys import *
from collections import *
from math import *

def shortestSupersequence(a: str, b: str) -> str:
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        dp[i][0] = 0
    for j in range(len(b) + 1):
        dp[0][j] = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = len(a)
    j = len(b)
    ans = ''

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            ans += a[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                ans += a[i - 1]
                i -= 1
            else:
                ans += b[j - 1]
                j -= 1

    while i > 0:
        ans += a[i - 1]
        i -= 1
    while j > 0:
        ans += b[j - 1]
        j -= 1
    
    ans = ''.join(reversed(list(ans)))

    return ans

