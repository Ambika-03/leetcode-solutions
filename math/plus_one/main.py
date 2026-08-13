class Solution:
  def plusOne(self, digits: list[int]) -> list[int]:
    number = ""
    for i in digits:
      number += str(i)

    number = int(number) + 1
    output_digits = []

    for i in str(number):
      output_digits.append(int(i))

    return output_digits
    
if __name__ == "__main__":
  solution = Solution()
  print(solution.plusOne([2, 3, 5]))
