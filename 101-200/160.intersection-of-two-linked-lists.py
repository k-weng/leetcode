# *************************************************************************
# Source: https://leetcode.com/problems/intersection-of-two-linked-lists/
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
# 
# For example, the following two linked lists:
# 
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.
# 
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# *************************************************************************

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, head_a, head_b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = head_a
        b = head_b
        
        while a is not b:
            a = a.next if a else head_b
            b = b.next if b else head_a
        return a
