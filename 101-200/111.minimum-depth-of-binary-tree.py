# *************************************************************************
# Source: https://leetcode.com/problems/minimum-depth-of-binary-tree/
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
# return its minimum depth = 2.
# *************************************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        if min(left_min, right_min):
            return min(left_min, right_min) + 1
        else:
            return max(left_min, right_min) + 1

# Iterative Solution
class Solution(object):
    def minDepth(self, root):
        depth = 0
        level = [root]
        
        while root and level:
            depth += 1
            curr_level = []
            for node in level:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    curr_level.append(node.left)
                if node.right:
                    curr_level.append(node.right)
            level = curr_level
        return depth