# *************************************************************************
# Source: https://leetcode.com/problems/remove-linked-list-elements/
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# *************************************************************************

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Recursive Solution
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        head.next = self.removeElements(head.next, val)

        return head.next if head.val == val else head
    
# Iterative Solutioin
class Solution(object):
    def removeElements(self, head, val): 
        if not head:
            return None
        
        curr = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head.next if head.val == val else head
