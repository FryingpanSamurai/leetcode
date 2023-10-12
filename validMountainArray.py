class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        # 0->3 inc, 3->2 dec
        # [0, 3, 2, 1]
        if arr == None or len(arr) < 3:
            return False
        
        i = 0

        # as long as we're increasing
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1

        # check peak [where increasing stops check value of i] 
        # (first or last peak will not be a valid mountain)
        if i == 0 or i == len(arr) - 1:
            return False

        # as long as we're decreasing
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1
        
        return i == len(arr) - 1

        

if __name__ == "__main__":
    testob = Solution()
    nums = [0, 2, 3, 4, 5, 2, 1, 0]
    print(testob.validMountainArray(nums))