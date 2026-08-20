## Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

# Example 2: 
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 step
3. 2 step + 1 step

#   Constraints: 
1 <= n <= 45

-----------------------------

# Core Idea
Answer for n depends only on previous two answers(n-1 and n-2)

# Efficient Approach
Insted of recursion, Calculate the value from left to right and keep only the previous two results
Note - previous and current store answers, not stair numbers

# Complexity
Time: O(n)
Space: O(1)