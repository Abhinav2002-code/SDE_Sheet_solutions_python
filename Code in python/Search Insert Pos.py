class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        if target > nums[high]:
            return high+1
        elif target < nums[low]:
            return low

        while low < high:
            mid = (low + high) //2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
        if high - low <= 1 and target > nums[low]:
                return low+1
        return low 

