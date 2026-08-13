You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large interger does not contain any leading 0's.

Increment the large integer by one an dreturn the resulting array of digits.

# Example 1:
Input: digits = [1, 2, 3]
Output: [1, 2, 4]
Explanation: `The array represents the integer 123. 
Incrementing by one gives 123 + 1 = 124
Thus, the result should be [1, 2, 4]`

# Example 2:
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
Explanation: `The array represents the integer 4321/
Incrementing by one gives 4321 + 1 = 4322
Thus, the result should be [4, 3, 2, 2]`

# Example 3:
Input: digits = [9]
Output: [1, 0]
Explanation: `The array represents the integer 9. 
Incrementing by one gives 9 + 1 = 10
Thus, the result should be [1, 0]`

## Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.

---------------------------

# Approach
I solved this by converting the digit array into a number, adding 1, and then converting the result back into a digit array.

----------------------------
# Steps
1. Start with an empty string.
2. Convert each digit to a string and append it. `[2, 3, 5] -> "235"`
3. Convert the string to an integer and add 1.  `235 + 1 -> 236`
4. Convert the result back to a string.
5. Convert each character back to an integer and store it in a new list.  `"236" -> [2, 3, 6]`

----------------------------
# Complexity

-Time: O(n) - traverse the digits and the resulting number
- Space: O(n) - store the number as a string and the output list.