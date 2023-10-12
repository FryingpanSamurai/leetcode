class Solution:
    def mergeAlternatively(self, word1: str, word2: str,) -> str: 
        merged_word = ""
        # merge the strings by adding letters in alternating order starting with word1
        # if one string is longer than the other append the remaining str onto end

        # take two pointers
        word1_ptr = 0
        word2_ptr = 0

        # to keep track of alternating sequence
        main_ptr = 0

        # cycle through the longest string
        while main_ptr < (len(word1) + len(word2)):
            # if letter exists in the word1 and our main pointer is even
            if word1_ptr < len(word1) and main_ptr % 2 == 0:
                merged_word += word1[word1_ptr]
                word1_ptr += 1
            elif word2_ptr < len(word2):
                merged_word += word2[word2_ptr]
                word2_ptr += 1
            else:
                merged_word += word1[word1_ptr]
                word1_ptr += 1
            main_ptr += 1
        return merged_word
            

if __name__ == '__main__':
    word1 = "abc"
    word2 = "pqr"
    word3 = "ghi"
    word4 = "j"
    test_cases = [[word1, word2],[word3, word4]]
    test = Solution()
    
    for testcase in test_cases:
        print(test.mergeAlternatively(testcase[0], testcase[1]))