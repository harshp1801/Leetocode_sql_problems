class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Here m is the first m elements that needs to be merged 
        last_ind = m + n - 1 # the last index of nums1 array

        while m>0 and n>0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_ind] = nums1[m - 1]
                m-=1
            else:
                nums1[last_ind] = nums2[n - 1]
                n-=1
            last_ind-=1
        while n > 0:
            nums1[last_ind] = nums2[n - 1]
            n,last_ind = n - 1,last_ind - 1

        return nums1