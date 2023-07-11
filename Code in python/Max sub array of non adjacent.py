from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    n = len(nums)
    prev = nums[0]
    prev2 = 0
    for i in range(1,n):
        take = nums[i]
        if i > 1:
            take += prev2
        nottake = 0 + prev

        curri = max(take,nottake)
        prev2 = prev
        prev = curri
    return prev