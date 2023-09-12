'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len (s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

'''
To solve this problem, the provided code defines a class called Solution with a method longestCommonPrefix that takes an array of strings strs as input. Here's an explanation of how the code works:

Initialize an empty string res to store the longest common prefix.

Iterate through the characters of the first string in the array strs[0] using a for loop.

Inside the outer for loop, iterate through each string s in the strs array using another for loop. This inner loop compares the current character of strs[0] with the character at the same position in each string s.

If at any point during the inner loop, one of the following conditions is met, the function returns the current value of res as the longest common prefix:

The index i is equal to the length of the string s (i.e., we have reached the end of s).
The character s[i] is not equal to the character in strs[0][i].
If none of the above conditions are met during the inner loop for all strings s, it means that the current character at index i is a part of the common prefix. Therefore, we append this character to the res string.

Continue iterating through the characters of the first string and repeating the above steps until one of the conditions mentioned in step 4 is met.

After the loop completes, return the res string, which contains the longest common prefix among all the strings in the input array
'''