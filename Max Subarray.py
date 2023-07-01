class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxi = -sys.maxsize -1
        sums = 0
        for i in range(n):
            sums += nums[i]

            if sums > maxi:
                maxi = sums
            if sums < 0:
                sums =0
        return maxi


