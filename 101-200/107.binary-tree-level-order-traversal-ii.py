# *************************************************************************
# Source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
#
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.traverse(root, 1, result)
        return result

    def _traverse(self, root, level, result):
        if root:
            if len(result) < level:
                result.insert(0, [])

            self._traverse(root.left, level + 1, result)
            self._traverse(root.right, level + 1, result)
            result[-level].append(root.val)

# Iterative Solution
class Solution(object):
    def levelOrderBottom(self, root):
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
            
            result.insert(0, curr_level)
            level = next_level

        return result
