class Solution:
  def isPalindrome(self, x: int) -> bool:
    input_x = x
    reversed_x = 0
    
    while x > 0:
      last_digit = x % 10
      x = x // 10
      reversed_x = reversed_x * 10 + last_digit

    return input_x == reversed_x
  
if __name__ == "__main__":
  solution = Solution()
  is_palindrome = solution.isPalindrome(454)
  print(is_palindrome)