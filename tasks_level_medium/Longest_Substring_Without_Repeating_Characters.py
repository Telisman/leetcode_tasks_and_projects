'''
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substringwithout repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # Store the index of each character
        max_length = 0  # Store the maximum substring length
        start = 0  # Start of the current substring

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1  # Move the start to the next non-repeating character

            char_index[s[end]] = end  # Update the index of the current character
            max_length = max(max_length, end - start + 1)  # Update the maximum length

        return max_length

# Test the function
solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))  # Output: 3
