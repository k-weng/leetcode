# *************************************************************************
# Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.
# *************************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            left_max = self.maxDepth(root.left)
            right_max = self.maxDepth(root.right)
            return max(left_max, right_max) + 1

        return 0

# Iterative Solution
class Solution(object):
    def maxDepth(self, root):
        depth = 0
        level = [root]

        while root and level:
            depth += 1
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            level = next_level

        return depth
