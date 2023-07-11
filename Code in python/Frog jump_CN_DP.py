from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    dp = [0]*n
    dp[0] = 0

    for i in range(1,n):
        left = dp[i-1] + abs(heights[i] - heights[i-1])
        right = 2**63 - 1
        if i > 1:
            right = dp[i-2] + abs(heights[i] - heights[i-2])

        dp[i] = min(left,right)
    return dp[n-1]

    pass
