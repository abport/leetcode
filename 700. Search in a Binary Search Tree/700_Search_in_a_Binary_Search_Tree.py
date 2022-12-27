# Definition for a binary tree node.
# This is a class that represents a node in a binary tree.
# It has three instance variables: a value (val), and references to its left and right children (left and right).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # This is the constructor for the TreeNode class.
        # It initializes the node with a value (val) and references to its left and right children (left and right).
        # If no value is provided, the value is set to 0.
        # If no references to left and right children are provided, they are set to None.
        self.val = val
        self.left = left
        self.right = right

# This is the Solution class that contains the searchBST method.


class Solution:
    # This is the searchBST method that takes in a BST root node (root) and a value to search for (val).
    # It returns the subtree rooted at the node with the value val, or None if such a node does not exist in the BST.
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # If the root node is None, return None.
        if not root:
            return None

        # If the root node has a value equal to val, return the root node.
        if root.val == val:
            return root

        # If the root node has a value greater than val, search the left subtree.
        elif root.val > val:
            return self.searchBST(root.left, val)

        # If the root node has a value less than val, search the right subtree.
        else:
            return self.searchBST(root.right, val)
