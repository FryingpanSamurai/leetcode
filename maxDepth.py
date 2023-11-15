from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    FUNCTION:   Given a binary tree, determine the maximum depth of the tree.
                MAX DEPTH: Number of nodes along the longest path from the root node down to furthest leaf
    OUTPUT:     count of max depth as int
    INPUT:      root as Binary Tree
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # this implementation builds on the previous count
        # 1 + counts the current node in the recursion
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

if __name__ == '__main__':
    test = Solution()
    mytree = TreeNode(27, TreeNode(1, None, TreeNode(5)), TreeNode(3))
    testtree = None
    print(test.maxDepth(testtree))
