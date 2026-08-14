class Solution:
  def mySqrt(self, x:int) -> int:
    answer = 0
    for i in range(1, x + 1):
      if i * i <= x:
        answer = i

    return answer

if __name__ == "__main__":
  solution = Solution()
  sqrt = solution.mySqrt(50)
  print(sqrt)