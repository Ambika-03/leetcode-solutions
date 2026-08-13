Given two binary strings a and b, return their sum as a binary string.

# Example 1:
Input: a = "11", b = "1"
Output: "100"

# Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

# Constraints:
- 1 < a.length, b.length <= 10^4
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

----------------------------
## Approach
Python provides built-in functions to convert between binary and decimal.

# 1. Convert Binary -> Decimal
`int(binary_string, 2)` The 2 tells Python that the number is in base 2.
int("1010", 2) = 10
int("1101", 2) = 13

# 2. Add the Numbers
10 + 13 = 23

# 3. Convert Decimal -> Binary
`bin(23)` returns: 0b101111` 0b is Python's prefix for a binary number.
To remove `0b`: bin(23)[2:]

# Result: 10111

----------------------------
- Time Complexity: O(n)
- Space Complexity: O(n)