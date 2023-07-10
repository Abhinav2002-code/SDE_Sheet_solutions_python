class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = m + n -1
        right = 0

        while (left >= 0 and right < n):
            if(nums1[left] == 0 ):
                nums1[left],nums2[right] = nums2[right],nums1[left]
                left-=1
                right+=1
            
            else:
                break
        nums1.sort()
        # nums2.sort()
        
        return nums1
