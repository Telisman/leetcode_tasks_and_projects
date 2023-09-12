'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''


class Solution(object):
    def mergeTwoLists(self,list1,list2 ):
        head =ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next =list1
                list1=list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return head.next


'''
Initialize a new linked list head and a pointer current to manage the merged list.

head is initialized as an empty node (it does not contain any value).
current initially points to the head node.
Use a while loop to iterate through both list1 and list2 until at least one of them is exhausted (i.e., list1 or list2 becomes None).

Within the loop, compare the values of the current nodes in list1 and list2:

If the value of the current node in list1 is less than the value of the current node in list2, then:

Set current.next to list1 to add the current node from list1 to the merged list.
Move the list1 pointer to the next node in list1.
If the value of the current node in list2 is less than or equal to the value of the current node in list1, then:

Set current.next to list2 to add the current node from list2 to the merged list.
Move the list2 pointer to the next node in list2.
After adding a node to the merged list, move the current pointer to the newly added node. This keeps track of the last node in the merged list.

Once the loop terminates (i.e., when either list1 or list2 becomes empty), there may still be nodes left in the other list. To ensure that all nodes are included in the merged list, set current.next to the remaining non-empty list (either list1 or list2). This is achieved using the or operator.

Finally, return the head.next node as the head of the merged linked list. Note that we return head.next because the head node itself is empty and serves as a dummy node to simplify the logic
'''