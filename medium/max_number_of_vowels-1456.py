"""
Problem Title: Maximum Number of Vowels in a Substring of Given Length
Problem ID: 1456
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

Description:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Approach:
1. Find out how many vowels are in the first window.
2. Move the window next and check if the element leaving it and the element entering it are vowels
3. Return the result, which contains the maximum number of vowel letters in any window.
"""

vowels = {"a", "e", "i", "o", "u"}


def max_vowels(s: str, k: int) -> int:
    size = len(s)
    result = 0
    current_window = s[:k]
    for letter in current_window:
        if letter in vowels:
            result += 1
    i = 1
    current = result
    while i + k <= size:
        if s[i - 1] in vowels:
            current -= 1
        if s[i + k - 1] in vowels:
            current += 1
        result = max(result, current)
        i += 1
    return result


if __name__ == "__main__":
    string_input = "weallloveyou"
    window = 7
    print(max_vowels(string_input, window))
