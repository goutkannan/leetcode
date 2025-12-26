# 680. Valid Palindrome II

## Difficulty: Easy

## Problem Statement

Given a string `s`, return `true` if the `s` can be palindrome after deleting **at most one** character from it.

## Examples

**Example 1:**
```
Input: s = "aba"
Output: true
```

**Example 2:**
```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3:**
```
Input: s = "abc"
Output: false
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

---

## 🤔 Think Through These Questions

Before you start coding, consider:

1. **How is this different from Valid Palindrome I?**
   - What extra condition do we need to handle?

2. **What pointer technique should we use?**
   - Opposite direction? Same direction? Fast/slow?

3. **What happens when we find a mismatch?**
   - Can we just skip it and continue?
   - What are our options when characters don't match?

4. **How do we know if removing one character would work?**
   - Do we need to try multiple scenarios?

5. **Edge cases to consider:**
   - Already a palindrome?
   - Only one character?
   - Two characters?

---

## 💡 Hints (Don't peek until you've tried!)

<details>
<summary>Hint 1</summary>
Start with the standard two-pointer palindrome check (left and right).
</details>

<details>
<summary>Hint 2</summary>
When you find a mismatch, you have TWO choices: skip the left character OR skip the right character. Try both!
</details>

<details>
<summary>Hint 3</summary>
You can write a helper function to check if a substring is a palindrome.
</details>

<details>
<summary>Hint 4</summary>
If the string is already a palindrome without removing anything, that counts as deleting "at most one" (i.e., zero deletions).
</details>

---

## Approach

Write your approach here as you figure it out!
