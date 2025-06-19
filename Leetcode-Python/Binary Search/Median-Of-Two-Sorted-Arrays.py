class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        half = (len(A) + len(B)) // 2
        total = len(nums1) + len(nums2)
        if len(A) > len(B):
            A, B = B, A
        
        l = 0
        r = len(A) - 1

        while True:
            m = (l + r) // 2
            j = half - m - 2
            
            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m + 1] if (m + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Bright < Aleft:
                r = m - 1
            else:
                l = m + 1


