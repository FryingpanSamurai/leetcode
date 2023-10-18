class Solution:
  def addBinary(self, a: str, b: str) -> str:
    # method one
    # straight add the two binaries
    # 'NORMALIZE'
    if len(a) >= len(b):
      max_len = len(a)
      b = '0' * (len(a) - len(b)) + b
    else:
      max_len = len(b)
      a = '0' * (len(b) - len(a)) + a

    out_bin = ''
    placeholder = False

    for i in range(max_len-1, -1, -1):
      temp = int(a[i]) + int(b[i]) if not placeholder else int(a[i]) + int(b[i]) + 1

      if temp == 2:
        placeholder = True
        out_bin = '0' + out_bin
      elif temp == 1:
        placeholder = False
        out_bin = '1' + out_bin
      elif temp == 3:
        placeholder = True
        out_bin = '1' + out_bin
      else:
        placeholder = False
        out_bin = '0' + out_bin

    if placeholder:
      out_bin = '1' + out_bin

    return out_bin




if __name__ == '__main__':
  test = Solution()
  a1 = '11'
  b1 = '1'
  a10 = '1011'
  b10 = '1011'
  print(test.addBinary(a1, b1))
  print(test.addBinary(a10, b10))