def hasCycle(head):
    # We will use the "hare and tortoise" algorithm to detect a cycle
    # in the linked list. This means that we will have two pointers,
    # one that moves faster (the hare) and one that moves slower (the
    # tortoise). If there is a cycle in the linked list, the hare will
    # eventually catch up to the tortoise.

    # Initialize the hare and tortoise pointers
    hare = head
    tortoise = head

    # Loop until the hare or tortoise pointers are None (which means
    # we have reached the end of the linked list)
    while hare is not None and tortoise is not None:
        # Move the hare two steps forward
        hare = hare.next
        if hare is not None:
            hare = hare.next
        else:
            # If the hare is None, then there is no cycle
            return False

        # Move the tortoise one step forward
        tortoise = tortoise.next

        # If the hare and tortoise pointers are the same, then there
        # is a cycle in the linked list
        if hare == tortoise:
            return True

    # If we reach this point, then there is no cycle in the linked list
    return False
