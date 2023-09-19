'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''


# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         res = ''
#         resLen = 0
#
#         for i in range(len(s)):
#             # odd lenght
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > resLen:
#                     res = s[l:r + 1]
#                     resLen = r - l + 1
#                     l -= 1
#                     r += 1
#             # even lenght
#             l, r = i, i + 1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > resLen:
#                     res = s[l:r + 1]
#                     resLen = r - l + 1
#                 l -= 1
#                 r += 1
#
#         return res
# overtime - this code is working but it take to much time to proces

class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l + 1:r]

        result = ""
        for i in range(len(s)):
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
            sub2 = expand(i, i + 1)
            if len(sub2) > len(result):
                result = sub2
        return result

'''
def expand(l, r): is a helper function defined within the longestPalindrome method. It takes two indices l and r as arguments and returns the longest palindromic substring centered at these indices. It does this by expanding outward from the center (the indices l and r) while checking if the characters at those positions are the same. If they are the same, it continues expanding; otherwise, it stops and returns the palindromic substring found.

result = "" initializes an empty string result to store the longest palindromic substring found.

The code uses a for loop to iterate through each character in the input string s. For each character at index i, it does the following:

sub1 = expand(i, i): This line calls the expand function with both l and r set to i. It looks for a palindromic substring centered at the current character i. This substring can have an odd length, so it checks characters to the left and right of i. If it finds a longer palindromic substring than the current result, it updates result with this substring.
sub2 = expand(i, i + 1): This line calls the expand function with l set to i and r set to i + 1. It looks for a palindromic substring centered between the current character i and the next character i + 1. This substring can have an even length. If it finds a longer palindromic substring than the current result, it updates result with this substring.
Finally, the result variable contains the longest palindromic substring found among all possible substrings in the input string s, and it is returned as the output of the longestPalindrome method.
'''