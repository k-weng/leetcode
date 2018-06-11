# *************************************************************************
# Source: https://leetcode.com/problems/binary-tree-inorder-traversal/
#
# Given a binary tree, return the inorder traversal of its nodes' values.
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
# Output: [1,3,2]
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        return self._traverse(root, result)

    def _traverse(self, root, result):
        if root:
            result = self._traverse(root.left, result)
            result.append(root.val)
            result = self._traverse(root.right, result)

        return result

# Iterative Solution
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        done = False
        curr = root
        
        while not done and root:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if stack:
                    curr = stack.pop()
                    result.append(curr.val)
                    curr = curr.right
                else:
                    done = True
        
        return result
