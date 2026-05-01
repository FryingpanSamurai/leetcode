class Solution:
    def prefixExample(nums, queries, limit):
        # return a boolean array that represents the answer to each query
        # query is true if the sum of the subarray [x, y] from x to y 
        # is less than limit, false otherwise

        # so lets start making the prefix array
        prefix = [nums[0]]
        output = []
        n = len(nums)
        for i in range(1, n):
            prefix.append(nums[i] + prefix[len(prefix) - 1])
        
        for start, end in queries:
            # so we grab the end minus the start + first value of the original subarray 
            # (as we end up removing it with the first operation)
            ans = prefix[end] - prefix[start] + nums[start]
            output.append(ans < limit)
        return print(output)
    
if __name__ == "__main__":
    nums = [1,6,3,2,7,2]
    queries = [[0,3], [2,5], [2,4]]
    limit = 13
    Solution()
    Solution.prefixExample(nums, queries, limit)