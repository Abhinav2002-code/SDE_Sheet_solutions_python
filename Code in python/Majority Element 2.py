class Solution(object):
    def majorityElement(self, nums):
        n = len(nums) // 3
        freq = {}
        result = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num,count in freq.items():
            if count > n:
                result.append(num)
        return result
