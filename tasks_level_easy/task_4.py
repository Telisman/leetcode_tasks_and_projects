'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefor it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefor  it is not a palindrome.

Constraints: -231 <= x <= 231 - 1
Follow up: Could you solve it without converting the integer to a string?
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10: return False
            x = (x % div) // 10
            div = div // 100
        return True
'''
Check if x is negative: If x is negative, it cannot be a palindrome because the '-' sign at the beginning makes it different when read in reverse. So, if x is negative, the function returns False immediately.

Initialize a variable div to 1: This variable is used to determine the divisor to extract the leftmost and rightmost digits of x.

Use a while loop to find the appropriate divisor div:

In this loop, we repeatedly multiply div by 10 until it's larger than or equal to x. This helps us find the divisor that allows us to extract the leftmost digit of x.
After finding the divisor div, we enter another while loop:

In this loop, we continue processing x until it becomes zero.
At each step, we compare the leftmost and rightmost digits of x by using integer division and modulus operations.
If the leftmost digit (obtained by x // div) is not equal to the rightmost digit (obtained by x % 10), we return False, indicating that x is not a palindrome.
We then update x by removing both the leftmost and rightmost digits. We do this by taking the remainder of x after dividing by div, and then performing integer division by 10. Additionally, we update div by dividing it by 100, as we've removed two digits from x.
If we reach this point without finding any mismatched digits, it means x is a palindrome, and we return True.
'''
