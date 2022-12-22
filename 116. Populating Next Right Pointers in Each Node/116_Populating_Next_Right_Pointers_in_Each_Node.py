def connect(root):
    if not root:
        return

    # initialize a queue with the root node
    queue = [root]

    # traverse the tree level by level
    while queue:
        # get the size of the current level
        size = len(queue)

        # iterate over all the nodes on the current level
        for i in range(size):
            # get the next node
            node = queue.pop(0)

            # set the next pointer of the current node
            if i < size - 1:
                node.next = queue[0]

            # add the left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root
