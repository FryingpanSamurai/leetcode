class Solution:
  def lemonadeChange(self, bills: list[int]) -> bool: 
    tens = fives = 0
    for bill in bills:
      if bill == 5:
        fives += 1
      elif bill == 10 and fives >= 1:
        tens += 1
        fives -= 1
      elif bill == 20 and fives >= 3:
        fives -= 3
      elif bill == 20 and (fives >= 1 and tens >= 1):
        fives -= 1
        tens -= 1
      else:
        return False

    return True
if __name__ == '__main__':
  test = Solution()
  bills = [5,5,5,10,20]
  test.lemonadeChange(bills)