Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

## Contraints:
0 <= x <= 2^31 - 1

-------------------------------

## My Approach
I used a simple for loop to check every number starting from 1.

For each number i:
i * i <= x

If this condition is true, i can be the square root, so I store it in answer.

The loop continues because there might be a larger number whose square is still less than or equal to x.

---------------------------------

## Why does this work?
We need the largest integer i whose square is less than or equal to x.

In other words: `i^2 <= x`
Once i^2 becomes greater than x, no larger number can be the answer.
The answer variable remembers the last valid number.

---------------------------------

# Time Complexity
O(x) - I the worst case, the loop checks numbers from 1 to x.

# Space Complexity
O(1) - Only a few variables are used, regardless of the input size.