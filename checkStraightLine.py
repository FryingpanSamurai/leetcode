class Solution:
  def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
    """
      INSTRUCTIONS:
        you are given coordinates, coordinates[i] = [x, y] where [x, y]
        represents the coordinates of a point.

        check if these points make a straight line
    """
    # LETS SEE IF THE COORDINATES SATISFY THE EQUATION y = mx+b
    # WHERE b = y-int or where x = 0
    # can also determine slope where m = rise / run = y1 - y0 / x1 - x0
    # if the slope remains constant through the coords then it should be straight
    try:
      m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
      for i in range(len(coordinates) - 1):
        m_new = (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0])
        if m_new != m:
          return False
        else:
          continue
      return True
    except:
      for i in range(len(coordinates) - 1):
        if coordinates[i+1][0] - coordinates[i][0] == 0:
          continue
        else:
          return False
      return True
      

if __name__ == '__main__':
  test = Solution()
  coords = [[0,0],[0,1],[0,-1]]
  print(test.checkStraightLine(coords))