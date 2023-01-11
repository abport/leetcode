class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # create a list of empty lists, one for each node in the tree
        adj = [[] for _ in range(n)]
        # iterate over the edges in the tree, adding each edge to the adjacency list of both nodes
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            # initialize total time required to collect all apples to 0
            total_time = 0
            # visit all children of the current node
            for child in adj[node]:
                if child == parent:
                    # skip visiting parent node again
                    continue
                # recursively visit the child node, and add the time required to collect all apples in the subtree rooted at the child
                child_time = dfs(child, node)
                if child_time or hasApple[child]:
                    total_time += child_time + 2
            return total_time

        # start dfs from the root node (node 0), with -1 as the parent node
        return dfs(0, -1)
