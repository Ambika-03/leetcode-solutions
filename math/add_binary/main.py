class Solution:
  def addBinary(self, a: str, b: str) -> str:
    sum = int(a, 2) + int(b, 2)
    return str(bin(sum)[2:])

if __name__ == "__main__":
  solution = Solution()
  add_binary = solution.addBinary("101", "1001")
  print(add_binary)