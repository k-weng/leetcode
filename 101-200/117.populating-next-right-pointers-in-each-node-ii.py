# *************************************************************************
# Source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#
# Given a binary tree
# 
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# Example:
# 
# Given the following binary tree,
# 
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# After calling your function, the tree should look like:
# 
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL
# *************************************************************************

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    """
    :type root: TreeLinkNode
    :rtype: nothing
    """
    def connect(self, root):
        node = root
        level_head = TreeLinkNode(0)

        while node:
            curr = level_head
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = level_head.next
            level_head.next = None
