# This function takes in the head of a sorted linked list as input
# and returns the head of the linked list with duplicates removed
def removeDuplicates(head):
    # We start by creating a "current" variable to keep track of the current node
    # in the linked list. We set it to the head of the linked list
    current = head

    # Then, we use a while loop to iterate through the linked list
    while current:
        # We check if the next node in the linked list exists and if it has the same value
        # as the current node
        if current.next and current.next.val == current.val:
            # If the next node exists and has the same value as the current node,
            # we skip over the next node by setting the current node's next pointer
            # to the node after the next node
            current.next = current.next.next
        else:
            # If the next node does not have the same value as the current node,
            # we move on to the next node by setting the current node to the next node
            current = current.next

    # After we have removed all duplicates, we return the head of the linked list
    return head
