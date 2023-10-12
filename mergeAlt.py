class Solution:
    def mergeAlternatively(self, word1: str, word2: str) -> str:
        merged_word = ""

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged_word += word1[i]
            if i < len(word2):
                merged_word += word2[i]
        return merged_word

if __name__ == '__main__':
    word1 = "a"
    word2 = "def"
    test = Solution()
    test.mergeAlternatively(word1=word1, word2=word2)