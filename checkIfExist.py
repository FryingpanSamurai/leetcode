#Given an array arr of integers, check if there exist two indices i and j such that :
#    i != j
#    0 <= i, j < arr.length
#    arr[i] == 2 * arr[j]

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        if (arr == None or len(arr) == 0):
            return False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if j == i:
                    continue
                elif arr[j]/2 == arr[i] or arr[i]/2 == arr[j]:
                    return True
        return False

if __name__ == "__main__":
    testob = Solution()
    nums = [10, 2, 5, 3]
    nums2 = [3, 1, 7, 11]
    print(testob.checkIfExist(nums2))