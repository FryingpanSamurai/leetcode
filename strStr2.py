class Solution:
    def strStr(self, haystack: str, needle: str) -> str:
        # EDITORIAL PIECE
        # HASH ALGORITHM

        # strings map to their 'hashed valus'
        # but two strings that are equal in hash value are not necesarily the same chars

        # so, "abb" = 1 + 2 + 2 = 5
        # but so does "aca" = 1 + 3 + 1 = 5
        # however, we can use this property to check 
        # ONLY THOSE haystack-substrings whose hashed value is equal to needle
        # Spurious Hits will compromise this algorithm ramping the complexity to that of brute force
        # combat with rolling hash, in that index positions of char are weighted
        # the last value is 10**0, (assigning from right to left) 10**1, 10**2, and so on
        # yada, yada, yada the base number for radix needs to be >= 26 using modulus of a very large prime number
        # here's the algorithm:
        m = len(needle)
        n = len(haystack)
        if n < m:
            return -1

        # CONSTANTS
        RADIX = 26
        MOD = 1_000_000_033
        MAX_WEIGHT = 1

        for _ in range(m):
            MAX_WEIGHT = (MAX_WEIGHT * RADIX) % MOD

        # Function to compute the hash of m-String
        def hash_value(string):
            ans = 0
            factor = 1

            for i in range(m - 1, -1, -1):
                ans += ((ord(string[i]) - 97) * (factor)) % MOD
                factor = (factor * RADIX) % MOD

            return ans % MOD

        # Compute the hash of needle
        hash_needle = hash_value(needle)

        # Check for each m-substring of haystack, starting at window_start
        for window_start in range(n - m + 1):
            if window_start == 0:
                # Compute hash of the First Substring
                hash_hay = hash_value(haystack)
            else:
                # Update Hash using Previous Hash Value in O(1)
                hash_hay = ((hash_hay * RADIX) % MOD
                            - ((ord(haystack[window_start - 1]) - 97)
                            * MAX_WEIGHT) % MOD
                            + (ord(haystack[window_start + m - 1]) - 97)
                            + MOD) % MOD

            # If hash matches, Check Character by Character. 
            # Because of Mod, spurious hits can be there.
            if hash_needle == hash_hay:
                for i in range(m):
                    if needle[i] != haystack[i + window_start]:
                        break
                if i == m - 1:
                    return window_start

        return -1

if __name__ == '__main__':
    hs = ""
    ndl = ""
    test = Solution()
    test.strStr(hs, ndl)