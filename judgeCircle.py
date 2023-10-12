class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = 0
        robot = [0,0]
        x = robot[0]
        y = robot[1]
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            else:
                y -= 1
                
        if x == origin and y == origin:
            return True
        else:
            return False



if __name__ == '__main__':
    moves = "RLUD"
    test = Solution()
    test.judgeCircle(moves=moves)