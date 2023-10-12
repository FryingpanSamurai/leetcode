class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        def check_win(self) -> bool:
            return check_all(self)

        def check_all(self):
            if check_diagonal(self):
                return True
            elif check_diagonal_inv(self):
                return True
            elif check_rows(self):
                return True
            elif check_cols(self):
                return True
            else:
                return False

        def check_diagonal(self) -> bool:
            for i in range(3):
                if my_board[i][i] == playerChar and i != 2:
                    continue
                elif my_board[i][i] == playerChar and i == 2:
                    return True
                else:
                    return False
        
        def check_diagonal_inv(self) -> bool:
            x = 2
            y = 0
            for i in range(3):
                if my_board[x][y] == playerChar and x != 0 and y != 2:
                    x -= 1
                    y += 1
                    continue
                elif my_board[x][y] == playerChar and x == 0 and y == 2:
                    return True
                else:
                    return False


        def check_rows(self) -> bool:
            x = 0
            y = 0
            for i in range(3):
                for j in range(3):
                    if my_board[i][j] == playerChar and j != 2:
                        continue
                    elif j == 2 and my_board[i][j] == playerChar:
                        return True
                    else:
                        break
                
        def check_cols(self) -> bool:
            y = 0
            while y < 3:
                for i in range(3):
                    if my_board[i][y] == playerChar and i != 2:
                        continue
                    elif my_board[i][y] == playerChar and i == 2:
                        return True
                    elif my_board[i][y] != playerChar and i == 2:
                        return False
                    else:
                        y += 1
                        break
        # player A places 'X'
        # player B places 'O'
        # placed in EMPTY SQUARES ONLY
        # Game ends:
        # 1. THREE OF THE SAME CHAR FILLING ANY ROW
        # 2. ALL SQUARES ARE NON-EMPTY (keep total move counter ...< 9)
        
        # no more moves can be played if the game is over
        # moves[i] = [row, col] of ith move
        # return winner, draw, if there are still movements to play return pending
        # grid is always empty and A will start
        player = "A"
        playerChar = "X"
        my_board = [[0,0,0],[0,0,0],[0,0,0]]
        for idx, move in enumerate(moves):
            my_board[move[0]][move[1]] = str(playerChar)
            if check_win(self):
                return player
            elif len(moves) == 9 and idx == 8:
                return 'Draw'
            elif idx == len(moves) - 1 and len(moves) != 9:
                return 'Pending'
            else:
                if player == "A":
                    player = "B"
                    playerChar = "O"
                else:
                    player = "A"
                    playerChar = "X"




        

if __name__ == '__main__':
    moves = [[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]
    # X |  | 0
    # --------
    #   | X| 0
    # --------
    #   |  | X
    test = Solution()
    test.tictactoe(moves=moves)