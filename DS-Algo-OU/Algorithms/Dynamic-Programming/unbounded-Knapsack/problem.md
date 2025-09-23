# Problem: Unbounded Knapsack

## 📝 Problem Description

Given a list of items, where each item has a **weight** and a **value**, and a knapsack with a maximum weight **capacity**, your task is to determine the maximum total value that can be obtained.

The key difference in this version is that you have an **unlimited supply of each item**. You can take any item as many times as you want, as long as the total weight does not exceed the knapsack's capacity.

---


## Test Case 1: General Case
**Input**:

weights = [1, 3, 4]

[0,0,0,0,0,0,0,0]

values = [15, 40, 50]

capacity = 7

Expected Output: 90

**Explanation**: The optimal choice is to take one item of weight 3 (value 40) and one item of weight 4 (value 50).

Total weight = 3 + 4 = 7

Total value = 40 + 50 = 90


## Test Case 2: Greedy Choice is Not Optimal
**Input**:

weights = [3, 2]

values = [14, 9]

capacity = 6

Expected Output: 28

**Explanation**: A greedy approach based on value-to-weight ratio (14/3 ≈ 4.67 vs 9/2 = 4.5) might mislead you. The best solution is to take the item (w:3, v:14) twice.

Total weight = 3 + 3 = 6

Total value = 14 + 14 = 28

(Taking the other item three times would give a weight of 6 but a value of only 9 * 3 = 27).