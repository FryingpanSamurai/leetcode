class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n) -> None:
        # merge two sorted arrays in-place nums1
        # do this by creating two pointers and a head, doing a compare, replacing the value or continuing traversing the array
        # start at the end of the array to avoid O(n) operations like insert
        ptr1 = m - 1
        ptr2 = n - 1
        head = m + n - 1

        while ptr1 >= 0 and ptr2 >= 0:
            # larger number -> head
            if nums1[ptr1] > nums2[ptr2]:
                nums1[head] = nums1[ptr1]
                # decrement ptr1 and head
                ptr1 -= 1
                head -= 1
            else:
                nums1[head] = nums2[ptr2]
                ptr2 -= 1
                head -= 1
        
        # catch any remaining elements of nums2
        while ptr2 >= 0:
            nums1[head] = nums2[ptr2]
            ptr2 -= 1
            head -= 1
        print(nums1)

if __name__ == "__main__":
    nums1 = [1,3,5,0,0,0]
    nums2 = [2,4,6]
    test = Solution()
    test.merge(nums1, 3, nums2, 3)
