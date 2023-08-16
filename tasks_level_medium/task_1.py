'''
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)  # Dummy head to simplify the logic
        current = dummy_head  # Pointer to traverse the new linked list
        carry = 0  # Initialize carry to 0

        while l1 or l2:
            # Get the values of the current nodes, if available
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Get the carry by dividing by 10
            digit = total % 10  # Get the digit for the new node

            # Create a new node with the calculated digit
            current.next = ListNode(digit)

            # Move the pointers forward, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next  # Move the pointer of the result linked list

        if carry > 0:
            current.next = ListNode(carry)  # Add any remaining carry as a new node

        return dummy_head.next  # Return the result linked list (excluding the dummy head)
