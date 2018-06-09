# *************************************************************************
# Source: https://leetcode.com/problems/binary-tree-postorder-traversal/
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?
# *************************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        return self._traverse(root, result)

    def _traverse(self, root, result):
        if root:
            result.append(root.val)
            result = self._traverse(root.left, result)
            result = self._traverse(root.right, result)
        return result

# Iterative Solution
class Solution(object):
    def preorderTraversal(self, root):
        stack = [root]
        result = []
        
        while root and stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
