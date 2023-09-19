'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= num <= 3999
'''

class Solution:
    def intToRoman(self, num):
        buffer = ""
        for roman, value in ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1):
            buffer += (num//value) * roman
            num -= (num//value) * value
        return buffer


'''

buffer is initialized as an empty string. This string will store the Roman numeral representation of the input integer.

The code uses a for loop to iterate through a list of tuples, where each tuple contains a Roman numeral and its corresponding decimal value. For example, ("M", 1000) represents the Roman numeral "M" with a decimal value of 1000.

Inside the loop, the code performs the following steps for each tuple:

(num // value) calculates how many times the current decimal value can be subtracted from the input num. This gives you the count of Roman numeral symbols needed for the current value.

(num // value) * roman creates a string with the Roman numeral repeated the calculated number of times. For example, if num is 3 and the current tuple is ("I", 1), it will add "III" to the buffer.

num -= (num // value) * value subtracts the value of the Roman numeral symbols added to the buffer from the input num. This is done to update the remaining value that needs to be converted to Roman numerals.

The loop continues for all the Roman numeral symbols in descending order of their values, effectively converting the entire input number to its Roman numeral representation.

Finally, the method returns the buffer, which contains the Roman numeral representation of the input integer.
'''