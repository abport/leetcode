This is a solution for the coding problem [144. Binary Tree Preorder Traversal from LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/description) in Python:

## Solution for the Problem: 144. Binary Tree Preorder Traversal:

```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    # Edge case: if the root is None, return an empty list
    if not root:
        return []

    # Initialize a stack to store nodes that we need to visit in the future
    # and a result list to store the values of the nodes we visit
    stack = [root]
    result = []

    # Iterate until the stack is empty
    while stack:
        # Get the top element from the stack
        node = stack.pop()

        # Append the value of the node to the result list
        result.append(node.val)

        # If the node has a right child, push it onto the stack
        if node.right:
            stack.append(node.right)

        # If the node has a left child, push it onto the stack
        # We push the left child before the right child so that it is processed first
        if node.left:
            stack.append(node.left)

    # Return the result list
    return result
```

This solution has a time complexity of O(n), where n is the number of nodes in the tree, because we visit each node once. It has a space complexity of O(n), because the maximum size of the stack is equal to the maximum height of the tree, which is n in the worst case (skewed tree).
