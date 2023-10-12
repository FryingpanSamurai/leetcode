class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # initial pos: 0,0 facing North
        # G: go straight 1 unit
        # L: turn 90* left
        # R: turn 90* right
        # determine if robot is bound by a circle
        # calculate final vector (pos, direction) after execution
        # 
        x = 0
        y = 0
        moved = False
        compass = ['North', 'East', 'South', 'West']
        r_pos = [x,y]
        r_face = 'North'
        r_face_idx = 0

        def calcPosCoords(self, x, y, face, moved):
            if face == 'North':
                y += 1
            elif face == 'South':
                y -= 1
            elif face == 'West':
                x -= 1
            elif face == 'East':
                x += 1
            moved = True
            return [x, y, moved]
        
        def loopCompass(self, idx):
            if idx > len(compass) - 1:
                idx = 0
            elif idx < 0:
                idx = len(compass) - 1
            return idx
        
        # robot stays in circle iff (looking @ final vector): 
        # 1. it changes the direction it faces
        # ||
        # 2. it moves 0

        def checkCircleBool(self, face, r_pos) -> bool:
            if face != 'North' or (x == 0 and y == 0):
                return True
            else:
                return False

        for instruction in instructions:
            if instruction == "G":
                # go forward, but in what direction
                temp = calcPosCoords(self, x, y, r_face, moved)
                x, y, moved = temp[0], temp[1], temp[2]
            elif instruction == "R":
                r_face_idx += 1
                r_face_idx = loopCompass(self, r_face_idx)
                r_face = compass[r_face_idx]
            else:
                r_face_idx -= 1
                r_face_idx = loopCompass(self, r_face_idx)
                r_face = compass[r_face_idx]

        print(f'Robot Position: ({x}, {y})\nDirection: {r_face}\nMoved: {str(moved)}')
        return checkCircleBool(self, r_face, r_pos)

if __name__ == '__main__':
    instructions = "GLRLLGLL"
    test = Solution()
    print(test.isRobotBounded(instructions))