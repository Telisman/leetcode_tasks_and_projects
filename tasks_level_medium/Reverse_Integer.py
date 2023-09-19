'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
'''


# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         MAX_INT = 2 ** 31 - 1
#         MIN_INT = -2 ** 31
#         reverse = 0
#
#         while x != 0:
#             if (reverse > MAX_INT / 10 or reverse < MIN_INT / 10):
#                 return 0
#             digit = x % 10 if x > 0 else -x % 10
#             reverse = reverse * 10 + digit
#             x = math.trunc(x / 10)
#
#         return reverse


class Solution:
    def reverse(self, x):
        if("-" in str(x)):
            if(int("-" + str(int(str(x)[::-1][0:len(str(x))-1]))) > (-2**31)):
                return int("-" + str(int(str(x)[::-1][0:len(str(x))-1])))
            else:
                return 0
        else:
            if(int(str(x)[::-1]) < (2**31)-1):
                return int(str(x)[::-1])
            else:
                return 0



'''
The function reverse takes an integer x as input.

It first checks if x is negative by examining whether the '-' character is present in the string representation of x. If it's negative, the code enters the first conditional block.

Inside the first conditional block, the code reverses the digits of x using slicing: str(x)[::-1]. This operation effectively reverses the order of characters in the string representation of x. Then, it removes the last character using [0:len(str(x))-1].

The code converts the reversed string back to an integer by calling int().

It negates the integer by prepending a '-' sign.

It checks whether the negated integer is greater than the minimum allowed value for a 32-bit integer (-2^31). If it's within the range, it returns the negated reversed integer; otherwise, it returns 0 to comply with the problem's constraints.

If x is not negative, the code enters the second conditional block.

Inside the second conditional block, it reverses the digits of x in the same way as before, using slicing.

It converts the reversed string back to an integer using int().

It checks whether the integer is less than the maximum allowed value for a 32-bit integer (2^31 - 1). If it's within the range, it returns the reversed integer; otherwise, it returns 0.'''