## Two Sum
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
you can return the answer in any order.

# Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# Example 2:
Input: nums = [3, 2, 4], target = 9
Output: [1, 2]

# Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

## Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

# Follow-up: 
Can you come up with an algorithm that is less than O(n^2) time complexity?


-------------------------
# Approach
For each number, calculate its complement (target-value), check whether that complement was already seen (If yes, return number and its complement), and store each number with its index for future checks.

# Complexity
Time = O(n)
Space = O(n)