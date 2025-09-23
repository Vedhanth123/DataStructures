# Problem: Count Optimal Subsets (0/1 Knapsack)

## 📝 Problem Description

This problem adds a challenging twist to the classic 0/1 Knapsack. Your task is twofold:

1.  First, determine the **single maximum value** that can be achieved within the given `capacity`.
2.  Then, find out **how many different subsets of items** result in this exact maximum value.

You are still bound by the 0/1 property: each item can either be included in a subset or not.

---

## 🐍 Function Signature

Here is the recommended function signature in Python:

Test Case 1: Multiple Items Form an Optimal Subset
Input:

weights = [1, 2, 3]

values = [10, 20, 30]

capacity = 3

Expected Output: 2

Explanation: The maximum value that can be achieved is 30. There are two distinct ways to get this value:

By taking the single item (w:3, v:30).

By taking the items (w:1, v:10) and (w:2, v:20).

Test Case 2: Edge Case with Zero Capacity
Input:

weights = [1, 2, 3]

values = [10, 20, 30]

capacity = 0

Expected Output: 1

Explanation: The maximum value possible is 0. There is exactly one way to achieve this: by taking no items (the empty set).

