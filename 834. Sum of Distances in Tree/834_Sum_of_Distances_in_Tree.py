from collections import defaultdict


def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    # Create a dictionary to store the children of each node
    children = defaultdict(list)
    # For each edge in the list of edges, add the child to the parent's list of children
    for u, v in edges:
        children[u].append(v)
        children[v].append(u)

    # Initialize the answer array with n elements, each element being 0
    ans = [0] * n
    # Initialize the size array with n elements, each element being 1
    # This array will store the number of nodes in the subtree rooted at each node
    size = [1] * n

    def dfs(node, parent):
        # For each child of the current node
        for child in children[node]:
            # If the child is not the parent (to avoid counting the edge twice)
            if child != parent:
                # Recursively call dfs on the child
                dfs(child, node)
                # Add the number of nodes in the child's subtree to the current node's subtree
                size[node] += size[child]
                # Add the sum of distances between the child's subtree and the current node to the answer array
                ans[node] += ans[child] + size[child]

    def dfs2(node, parent):
        # For each child of the current node
        for child in children[node]:
            # If the child is not the parent (to avoid counting the edge twice)
            if child != parent:
                # Subtract the sum of distances between the child's subtree and the current node from the answer array
                ans[child] = ans[node] - size[child] + (n - size[child])
                # Recursively call dfs2 on the child
                dfs2(child, node)

    # Call dfs on the root node (node 0) with no parent
    dfs(0, None)
    # Call dfs2 on the root node (node 0) with no parent
    dfs2(0, None)

    # Return the answer array
    return ans
