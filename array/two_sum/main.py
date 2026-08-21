class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, value in enumerate(nums):
      needed = target - value
      if needed in seen:
        return [seen[needed], index]
      else:
        seen[value] = index

if __name__ == "__main__":
  solution = Solution()
  indices = solution.twoSum([2, 7, 11, 15], 9)
  print(indices)
  print(solution.twoSum([3, 2, 4], 6))
  print(solution.twoSum([3, 3], 6))