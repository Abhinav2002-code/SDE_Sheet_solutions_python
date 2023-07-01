# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        start = ListNode()
        start.next = head
        fast = start
        slow = start


        for i in range(1, n+1):
            fast = fast.next


        while fast.next != None:
            fast = fast.next
            slow = slow.next


        slow.next = slow.next.next


        return start.next
