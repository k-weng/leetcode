# *************************************************************************
# Source: https://leetcode.com/problems/binary-tree-preorder-traversal/
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        return self._traverse(root, result)

    def _traverse(self, root, result):
        if root:
            result = self._traverse(root.left, result)
            result = self._traverse(root.right, result)
            result.append(root.val)
        return result

# Iterative Solution
class Solution(object):
    def postorderTraversal(self, root):
        stack = [root]
        result = []
        
        while root and stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return result[::-1]
