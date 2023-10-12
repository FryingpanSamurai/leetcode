class Solution:
    def strStr(self, haystack: str, needle: str) -> str:
        # given two strings [haystack, needle]
        # return index of the first occurrence of needle in haystack
        # or -1 if needle is not part of haystack
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

if __name__ == '__main__':
    hs = "sadbutsad"
    ndl = "sad"
    test = Solution()
    test.strStr(hs, ndl)