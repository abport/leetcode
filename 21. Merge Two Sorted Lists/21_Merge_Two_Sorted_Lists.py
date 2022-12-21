# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Check if either list is empty
    if not list1:
        return list2
    if not list2:
        return list1

    # Initialize a new linked list to store the result
    merged_list = ListNode()
    current = merged_list

    # Compare the values of the two lists and add the smaller value to the result list
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If one of the lists is longer, add the remaining elements to the result list
    current.next = list1 or list2

    return merged_list.next
