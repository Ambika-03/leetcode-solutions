class Solution:
  def mySqrt(self, x:int) -> int:
    start = 0
    end = x
    answer = 0
    while start <= end:
      mid = (start + end) // 2
      if mid * mid > x:
        end = mid - 1
      elif mid * mid <= x:
        start = mid + 1
        answer = mid
    return answer

if __name__ == "__main__":
  solution = Solution()
  sqrt = solution.mySqrt(1)
  print(sqrt)