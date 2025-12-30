# 11. Container With Most Water

## Difficulty: Medium

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

**Notice** that you may not slant the container.

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
The lines at index 1 (height=8) and index 8 (height=7) form the container.
Area = min(8, 7) * (8 - 1) = 7 * 7 = 49
```

**Example 2:**
```
Input: height = [1,1]
Output: 1
```

**Example 3:**
```
Input: height = [4,3,2,1,4]
Output: 16
Explanation: The lines at index 0 (height=4) and index 4 (height=4) form the container.
Area = min(4, 4) * (4 - 0) = 4 * 4 = 16
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`