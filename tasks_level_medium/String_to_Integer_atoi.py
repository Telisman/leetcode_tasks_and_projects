'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


Example 1:
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.


Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
'''

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Remove leading whitespaces
        s = s.lstrip()

        # Check for empty string
        if not s:
            return 0

        # Step 2: Check for '+' or '-'
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Read in digits
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Step 4: Apply sign
        result *= sign

        # Step 5: Clamp to the 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result

'''
s = s.lstrip(): This line removes any leading whitespace characters from the input string s. It uses the lstrip() method to do this.

if not s:: This line checks if the string s is empty (i.e., if there are no characters left after removing leading whitespaces). If it's empty, it returns 0 as per the requirements.

sign = 1: We initialize a variable sign to 1 by default. This variable will be used to store the sign of the resulting integer.

if s[0] == '-':: This condition checks if the first character of the string is a minus sign ('-'). If it is, we set sign to -1 to indicate that the result should be negative, and then we remove the minus sign from the string by slicing s from the second character onwards (i.e., s = s[1:]).

elif s[0] == '+':: Similar to the previous step, this condition checks if the first character of the string is a plus sign ('+'). If it is, we simply remove the plus sign from the string by slicing s from the second character onwards.

result = 0: We initialize a variable result to store the integer value that we will compute.

for char in s:: This loop iterates through each character in the remaining string s after removing leading signs and whitespaces.

if char.isdigit():: Inside the loop, we check if the current character char is a digit (0-9). If it is, we update the result by multiplying it by 10 and adding the integer value of char. This allows us to build the integer value digit by digit.

else:: If the current character is not a digit (e.g., it's a space or a non-numeric character), we break out of the loop because we've finished reading the numeric part of the string.

result *= sign: After the loop, we apply the sign (either 1 or -1) to the result to make it positive or negative as required.

INT_MIN and INT_MAX are constants representing the minimum and maximum values of a 32-bit signed integer.

Finally, we check if the result is within the 32-bit integer range. If it's less than INT_MIN, we return INT_MIN, and if it's greater than INT_MAX, we return INT_MAX. Otherwise, we return the calculated result.
'''