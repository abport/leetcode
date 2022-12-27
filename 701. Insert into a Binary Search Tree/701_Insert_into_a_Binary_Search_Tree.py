# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            # If the root is None, return a new TreeNode with the given value
            return TreeNode(val)
        if val < root.val:
            # If the value to insert is smaller than the current node's value,
            # recursively call the function on the left child
            root.left = self.insertIntoBST(root.left, val)
        else:
            # If the value to insert is larger than the current node's value,
            # recursively call the function on the right child
            root.right = self.insertIntoBST(root.right, val)
        return root
