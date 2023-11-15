from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    FUNCTION:   Given a binary tree, determine the minimum depth of the tree.
                MIN DEPTH: Number of nodes along the shortest path from the root node down to nearest leaf
    OUTPUT:     count of min depth as int
    INPUT:      root as Binary Tree
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # NOTE: A LEAF IS A NODE WITH NO CHILDREN

        return

if __name__ == '__main__':
    test = Solution()
    mytree = TreeNode(27, TreeNode(1, None, TreeNode(5)), TreeNode(3))
    testtree1 = TreeNode(3, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None, None)))))
    testtree = None
    print(test.minDepth(testtree1))
