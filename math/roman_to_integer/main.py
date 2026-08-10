class Solution:
  def romanToInt(self, s: str) -> int:
    values = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }

    total = 0

    for i in range(len(s)):
      if (i + 1 < len(s)) and (values[s[i]] < values[s[i + 1]]):
        total -= values[s[i]]
      else:
        total += values[s[i]]

    return total
    
if __name__ == "__main__":
  solution = Solution()
  roman_to_int = solution.romanToInt("MCMXCIV")
  print(roman_to_int)
