# This function takes in a linked list (head) and an integer (val)
def removeElements(head, val):
    # We create a dummy node and set it as the head of the linked list
    # This is so that we don't have to worry about the case where the head node has a value of val
    dummy = ListNode(-1)
    dummy.next = head

    # We set our current node as the dummy node
    curr = dummy

    # We loop through the linked list until we reach the end
    while curr.next:
        # If the value of the next node is equal to val
        if curr.next.val == val:
            # We skip over the next node by setting the current node's next to the next node's next
            curr.next = curr.next.next
        # If the value of the next node is not equal to val
        else:
            # We move on to the next node
            curr = curr.next

    # We return the next node of the dummy node, which is the new head of the linked list
    return dummy.next
