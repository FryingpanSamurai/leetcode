class Solution:
    def calPoints(self, operations: list[str]) -> int:
        import math
        # begin: start with empty record
        # operations[i]: the ith operation you must apply to the record
        # integer x: record a new score of x
        # '+': record new scord that is the sum of the previous two scores
        # 'D': record a new score that is double of the prev score
        # 'C': invalidate the previous score, removing it from the record

        # return the sum of all the scores on the record after applying all the operations
        i = 0
        my_scores = []
        while i < len(operations):
            try:
                if int(operations[i]):
                    my_scores.append(int(operations[i]))
                i += 1
            except:
                if operations[i] == "D":
                    my_scores.append(my_scores[-1] * 2)
                elif operations[i] == "C":
                    my_scores.pop()
                elif operations[-2]:
                    my_scores.append(int(math.fsum(my_scores[-2:])))
                else:
                    my_scores.append(my_scores[-1])
                i += 1
        return int(math.fsum(my_scores))





if __name__ == '__main__':
    ops = ["5", "1", "2", "C", "D", "+"]
    test = Solution()
    test.calPoints(ops)