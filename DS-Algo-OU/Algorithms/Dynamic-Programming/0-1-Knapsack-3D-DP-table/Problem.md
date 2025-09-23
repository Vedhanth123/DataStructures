# Problem: Multi-dimensional Knapsack (0/1)

## 📝 Problem Description

Given a list of items, where each item has a **weight**, a **volume**, and a **value**, your task is to find the subset of items that yields the maximum possible total value.

The selection is constrained by two factors:
1.  The **total weight** of the selected items cannot exceed a given `max_weight`.
2.  The **total volume** of the selected items cannot exceed a given `max_volume`.

You can only take each item once (this is the "0/1" property).

---


# Test Cases
## Test Case 1: General Case

Input:

`weights = [1, 2, 3, 4]`

`volumes = [2, 1, 4, 5]`

`values = [10, 8, 12, 15]`

max_weight = 5

max_volume = 6

**Expected Output**: 22

### Explanation:
 Items 0 and 2 ((w:1, v:2, val:10) and (w:3, v:4, val:12)). Total weight = 4, Total volume = 6.


## Test Case 2: Volume is the Limiting Factor

Input:

`weights = [10, 20, 30]`

`volumes = [1, 1, 1]`

`values = [60, 100, 120]`

max_weight = 50

max_volume = 2

**Expected Output**: 220

### Explanation:
Items 1 and 2 ((w:20, val:100) and (w:30, val:120)). Total weight = 50, but we can't take all three because total volume would be 3, exceeding the limit of 2.