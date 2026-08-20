class Solution:
  def climbStairs(self, n:int) -> int:
    if n <= 2:
      return n
    previous = 1
    current = 2
    current_stair = 2
    for stair in range(3, n + 1):
      next = previous + current
      previous = current
      current = next
    return current
      

if __name__ == "__main__":
  solution = Solution()
  for i in range(1, 10):
    print(f"{i} = {solution.climbStairs(i)}")
