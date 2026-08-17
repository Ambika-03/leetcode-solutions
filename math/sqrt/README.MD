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

## Approach
A simple approach would be to check every number: 1^2, 2^2, 3^2,.. until the square becomes greater than x.
However, this can take a lot of iterations for a large number.

Instead, we use `Binary Search`.

The possible answer is somewhere between 0 and x, so we start with: `start = 0, end = x`

We then choose the middle number: `mid = (start + end) // 2` and check whether mid * mid is smaller than, equal to, or greater than x.

# Why Binary Search Works
The array is sorted

----------------------------------

# Time Complexity
O(logx)

# Space Complexity
O(1)