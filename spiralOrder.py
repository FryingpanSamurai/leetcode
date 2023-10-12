class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        
        out_mat = []
        #### DESTRUCTIVE ####
        while matrix:
            # pop the first row and append the elements to out_mat
            out_mat += matrix.pop(0)

            # last col
            # row + 1, col
            if matrix and matrix[0]: # have to check row and col for col operations
                for row in matrix:
                    out_mat.append(row.pop())

            # last row rev
            # row, col - 1
            if matrix:
                out_mat += matrix.pop()[::-1] # start:end:step

            # first col rev
            # row - 1, col
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    out_mat.append(row.pop(0))

        return out_mat



if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    mat2 = [[7],[9],[6]]
    test = Solution()
    print(test.spiralOrder(mat1))