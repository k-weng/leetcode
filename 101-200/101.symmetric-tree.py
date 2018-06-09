# *************************************************************************
# Source: https://leetcode.com/problems/symmetric-tree/
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# *************************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._traverse(root.left, root.right) if root else True
    
    def _traverse(self, left, right):
        if left and right and left.val == right.val:
            return self._traverse(left.left, right.right) and \
                   self._traverse(right.left, left.right)
        return not left and not right


# Iterative Solution
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        stack = [[root.left, root.right]]
        
        while stack:
            left, right = stack.pop()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            
            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])

        return True
