class Solution:
  """
  FUNCTION:  Calculate x to the power n manually (without library functions)
  INPUT:     <x:float>, <n:int>
  OUTPUT:    <product:float>
  """
  def pow(self, x: float, n: int) -> float:
    # first thing to do...
    # use cases for n being 0, pos, or neg
    if n == 0:
      return 1
    elif n > 0:
      prod = 1
      # loop n times to get result
      for _ in range(n):
        prod *= x
      return prod
    else:
      # same thing just inverse
      prod = 1
      for _ in range(abs(n)):
        prod *= 1/x
      return prod

if __name__ == '__main__':
  test = Solution()
  x = 2.00
  n = 3
  print(test.pow(x, n))