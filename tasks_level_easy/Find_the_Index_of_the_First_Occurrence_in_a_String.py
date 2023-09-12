'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

'''
First, the code checks if the needle is an empty string. If needle is empty, it returns 0, indicating that an empty string is always found at the beginning of any other string.

Next, the code iterates through the haystack string using a for loop. The loop runs from 0 to len(haystack) - len(needle), where len(haystack) is the length of the haystack string, and len(needle) is the length of the needle string. This is because there's no need to check beyond this point since it's impossible for needle to fit within the remaining characters of haystack.

Inside the loop, the code extracts a substring from haystack starting at index i and extending to i + len(needle). This substring has the same length as needle and represents a window of characters in haystack.

The code then compares this extracted substring with the needle string. If they are equal, it means that we've found a match, and the method returns the index i, which represents the starting position of the first occurrence of needle in haystack.

If the loop completes without finding any matches, the method returns -1, indicating that needle is not part of haystack
'''