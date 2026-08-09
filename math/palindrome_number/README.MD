Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2: 
Input: x = -121
Output: False
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Contraints:
-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?

-----

## Approach
Reverse the number mathematically instead of converting it to a string.

## Key Concepts
- `% 10` -> gets the last digit
- `//10` -> removes the last digit
- `reversed_x * 10 + last_digit` -> builds the reversed number

-----

## Complexity
- Time: O(log x)
- Space: O(1)