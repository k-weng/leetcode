# *************************************************************************
# Source: https://leetcode.com/problems/copy-list-with-random-pointer/
#
# A linked list is given such that each node contains an additional random 
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# *************************************************************************

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        curr = head

        while curr:
            copy = RandomListNode(curr.label)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        dummy = copy = RandomListNode(0)
        curr = head
        
        while curr:
            next = curr.next.next
            
            copy.next = curr.next
            copy = copy.next
            
            curr.next = next
            curr = next

        return dummy.next
