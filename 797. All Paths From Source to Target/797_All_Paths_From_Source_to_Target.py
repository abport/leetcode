# Save the number of nodes in the graph
  self.n = len(graph)

   # Define a helper function that will find all paths from a given node to the target node
   def dfs(i):
        # If the current node is the target node, return a list with a single path (just the target node)
        if i == self.n - 1:
            return [[self.n - 1]]
        # If the current node has no outgoing edges, return an empty list
        if len(graph[i]) == 0:
            return [[]]

        # Initialize an empty list to store the paths
        res = []
        # Iterate through the list of nodes that can be reached from the current node
        for j in graph[i]:
            # Find all paths from the next node to the target node
            for path in dfs(j):
                # If the path is not empty (i.e., it reaches the target node),
                # append the current node to the path and add it to the list of paths
                if len(path) > 0:
                    res.append([i] + path)
        # Return the list of paths
        return res

    # Start the search at the source node (node 0)
    return dfs(0)
