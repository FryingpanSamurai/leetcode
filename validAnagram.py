class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        # using the previous hashed value argument
        # wouldn't the hashed value of an anagram be the same as the original?
        # TEST CASE 25 FOUND A BUG
        # TURNS OUT, MULTIPLE A's WILL NOT BE COUNTED IN THE RESULTING HASHVALUE
        # AAAAAA == AA, not good
        # so, a has to be 1 and so on
        # spurious hits strike again, hashed values without weight- not good
        # hm, ok order doesn't matter so why would weight
        # maybe hashed values don't work(?)
        # I've already solved this with dictionary so
        # TODO: HAVE TO SUBMIT AS DICTIONARY
        # easy way to solve with sort and if equal then true
        sorted_s = [ord(x) for x in s]
        sorted_t = [ord(x) for x in t]
        sorted_s.sort()
        sorted_t.sort()
        sorted_sn = [chr(x) for x in sorted_s]
        sorted_tn = [chr(x) for x in sorted_t]
        return "".join(sorted_sn) == "".join(sorted_tn)
            

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    test = Solution()
    test.validAnagram(s, t)