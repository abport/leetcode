# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list
        if not head:
            return head

        # Initialize previous node and current node
        prev_node = None
        curr_node = head

        # Iterate through the list
        while curr_node:
            # Save the next node
            next_node = curr_node.next
            # Reverse the link by pointing the current node's next pointer to the previous node
            curr_node.next = prev_node
            # Update the previous node to be the current node
            prev_node = curr_node
            # Update the current node to be the next node
            curr_node = next_node

        # Return the reversed list
        return prev_node
