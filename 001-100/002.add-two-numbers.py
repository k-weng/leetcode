# *************************************************************************
# Source: https://leetcode.com/problems/add-two-numbers/
#
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# *************************************************************************

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
        # self.next = None

# Recursive Solution
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=False):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2 and not carry:
            return None

        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        node = ListNode(sum % 10)

        node.next = self.addTwoNumbers(l1.next if l1 else None,
                                       l2.next if l2 else None,
                                       sum / 10)
        return node

# Iterative Solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry /= 10

        return dummy.next
