'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"


Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows == 1 or numRows >= len(s):
#             return s
#         rows = [[] for row in range(numRows)]
#         index = 0
#         step = 1
#         for char in s:
#             rows[index].append(char)
#             if index == 0:
#                 step = 1
#             elif index == numRows - 1:
#                 step = -1
#                 index += step
#         for i in range(numRows):
#             rows[i] = ''.join(rows[i])
#         return ''.join(rows)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ['' for _ in range(numRows)]
        index = 0
        step = 1

        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(rows)
'''

The convert function takes two parameters: s (the input string) and numRows (the number of rows in the zigzag pattern).

The code checks two special cases:

If numRows is equal to 1 or greater than or equal to the length of the input string s, there is no need to perform any conversion. In this case, the function returns the original string s as there is only one row or as many rows as the length of the string, which means the zigzag pattern is essentially a straight line.
If neither of the special cases applies, the code initializes a list called rows to hold the characters in each row of the zigzag pattern. The list is created with numRows empty strings, one for each row.

Two variables are initialized: index and step. index represents the current row in which the next character from the input string s should be placed, and step represents the direction of movement (either up or down the zigzag pattern).

The code then iterates through each character in the input string s:

a. It appends the current character to the corresponding row in the rows list. The index variable determines which row is the current row.

b. It checks whether index is at the top row (0) or at the bottom row (numRows - 1). If index is at the top row, it means the next character should be placed in the row below, so step is set to 1 (moving down). If index is at the bottom row, it means the next character should be placed in the row above, so step is set to -1 (moving up).

c. It updates the index variable by adding step to it, which determines the next row where the next character should be placed.

After processing all characters in the input string, the code joins the characters in each row of the rows list to form the final zigzag pattern as a single string.

Finally, the function returns the zigzag pattern as the output.
'''