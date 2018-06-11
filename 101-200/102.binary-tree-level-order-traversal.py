# *************************************************************************
# Source: https://leetcode.com/problems/binary-tree-level-order-traversal/
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# *************************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self._traverse(root, 1, result)

        return result
        
    def _traverse(self, root, level, result):
        if root:
            if len(result) < level:
                result.append([])

            result[level - 1].append(root.val)
            self._traverse(root.left, level + 1, result)
            self._traverse(root.right, level + 1, result)

# Iterative Solution
class Solution(object):
    def levelOrder(self, root):
        result = []
        level = [root]

        while root and level:
            curr_level = []
            next_level = []

            for node in level:
                curr_level.append(node.val)

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)
    
            result.append(curr_level)
            level = next_level

        return result
