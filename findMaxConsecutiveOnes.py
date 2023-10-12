def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    max_ones = 0
    zeroes = 0
    start = 0
    end = 0

    # Sliding Window [->...->]
    while end < len(nums):
        if nums[end] == 0:
            zeroes += 1
        
        # contract the window 
        while zeroes == 2:
            if nums[start] == 0:
                zeroes -= 1
            start += 1

        # +1 at end because second index arg is non-inclusive
        max_ones = max(max_ones, len(nums[start:end + 1]))
        end += 1

    return max_ones
