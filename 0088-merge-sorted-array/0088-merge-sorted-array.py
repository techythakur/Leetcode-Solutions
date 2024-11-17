class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1, n-1, (m+n)-1    # take 3 pointers to i points to nums1, j points to nums2, k points to end of nums1 i.e. (m+n)
        
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:  # compare which is bigger and place it to end of nums1 simultaneously
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
        while j>=0:    # if still some elements are left in nums2, place all of them in nums1
            nums1[k]=nums2[j]
            j-=1
            k-=1
            
        return nums1
        
        