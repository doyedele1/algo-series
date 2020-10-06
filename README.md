# Data Structures & Algorithms Series
In order to challenge myself and prepare for technical interviews, I decided to start this drill where I solve data structures & algorithms challenges. Questions are asked by top tech companies in the world

## 1. Reverse String
This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.

Example: Given the following strings...

```bash
"Cat", return "taC"
"The Daily Byte", return "etyB yliaD ehT"
"civic", return "civic"
```

## 2. Valid Palindrome
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.

Example: Given the following strings...

```bash
"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
```

## 3. Vacuum Cleaner Route
This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain ```L```, ```R```, ```U``` and ```D``` characters, representing left, right, up and down respectively.

Example: Given the following strings...

```bash
"LR", return true
"URURD", return false
"RUULLDRD", return true
```

## 4. Two Sum
This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, ```k```.

_Note: You may not sum a number with itself._

Example: Given the following arrays of integers...

```bash
"[1, 3, 8, 2], k = 10", return true
"[3, 9, 13, 7], k = 8", return false
"[4, 2, 6, 5, 2], k = 4", return true
```

## 5. Add Binary
This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s), return their sum (also as a binary string).

_Note: Neither binary string will contain leading 0s unless the string itself is 0._

Example: Given the following binary strings...

```bash
"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
```

## 6. Validate Characters
This question is asked by Google.  Given a string only containing the following characters ```(```, ```)```, ```{```, ```}```, ```[``` and ```]```, return whether or not the opening and closing characters are in a valid order.

Example: Given the following strings...

```bash
"(){}[]", return true
"(({[]}))", return true
"{(})", return  false
```

## 7. Valid Anagram
This question is asked by Facebook. Given two strings ```s``` and ```t```, return whether or not ```s``` is an anagram of ```t```.

Example: Given the following strings...

```bash
s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
```

## 8. Longest Common Prefix
This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.

_Note: You may assume all strings only contain lowercase alphabetical characters._

Example: Given the following arrays...

```bash
["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
```

## 9. Jewels and Stones
This question is asked by Amazon. Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

Example: Given the following jewels and stones...

```bash
jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
```

## 10. Valid Palindrome with Removal
This question is asked by Facebook. Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.

Example: Given the following strings...

```bash
"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
```

## 11. Intersection of Numbers
This question is asked by Google. Given two integer arrays, return their intersection.

_Note: The intersection is the set of elements that are common to both arrays._

Example: Given the following arrays...
```bash
nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
```
