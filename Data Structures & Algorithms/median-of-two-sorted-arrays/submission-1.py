class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        length = len(nums1) + len(nums2)
        half = length // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            mid = (l + r) // 2
            b_size = half - mid - 2

            aLeft = A[mid] if mid >= 0 else float("-inf")
            aRight = A[mid + 1] if mid + 1 < len(A) else float("+inf")

            bLeft = B[b_size] if b_size >= 0 else float("-inf")
            bRight = B[b_size + 1] if b_size + 1 < len(B) else float("+inf")

            
            if aLeft <= bRight and bLeft <= aRight:
                if length % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2

            if aLeft > bRight:
                r = mid - 1
            else:
                l = mid + 1
