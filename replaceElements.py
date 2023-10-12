import math

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # edge case
        if arr == None or len(arr) == 0:
            return arr

        # maxval init (traversing rear -> front)
        maxval = arr[len(arr) - 1]

        for i in range(len(arr)-1, -1, -1):
            temp = None
            if i == len(arr) - 1:
                arr[i] = -1
                continue

            if arr[i] > maxval:
                temp = arr[i]
                arr[i] = maxval
                maxval = temp
            else:
                arr[i] = maxval
        return arr


if __name__ == "__main__":
    testob = Solution()
    nums = [17,18,5,4,6,1]
    print(testob.replaceElements(nums))
