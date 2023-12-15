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
                Depth First Traversal: travels all the way down the binary tree, no break
                        {9}
                     1./  3.\
                    2./    4.\
    OUTPUT:     count of min depth as int
    INPUT:      root as Binary Tree
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # NOTE: A LEAF IS A NODE WITH NO CHILDREN

        # NULL root, do not add to count
        if not root:
            return 0
        
        # recurse through right or left depending on if child node exists (not a leaf)
        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        
        # find the lowest leaf through recursion
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

if __name__ == '__main__':
    test = Solution()
    mytree = TreeNode(27, TreeNode(1, None, TreeNode(5)), TreeNode(3))
    testtree1 = TreeNode(3, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None, None)))))
    testtree = None
    print(test.minDepth(testtree1))
