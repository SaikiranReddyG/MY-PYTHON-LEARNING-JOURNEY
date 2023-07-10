class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head: ListNode) -> bool:
    """initialize two nodes slowly and fast"""
    slow = fast = head
    """move the fast pointer to the head of the list"""
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    """reverse the seacond half of the list"""
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        slow = temp

    """comapre the 1st half and the reversed 2nd half"""

    while prev:
        if head.val != prev.val:
            return False

        head = head.next
        prev = prev.next

    return True



