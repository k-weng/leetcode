# *************************************************************************
# Source: https://leetcode.com/problems/reverse-linked-list/
#
# Reverse a singly linked list.
# 
# Example:
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you implement both?
# *************************************************************************

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Recursive Solution
class Solution(object):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def reverseList(self, head, prev=None):
        if not head:
          return prev
  
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)

# Iterative Solution
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            curr, head.next = head.next, prev
            prev = curr
        return prev