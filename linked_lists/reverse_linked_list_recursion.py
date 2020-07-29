# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def f(h, n=None):
    if h is None:
        return h
    if h.next is None:
        h.next = n
        return h
    poni = f(h.next ,h)
    h.next = n
    return poni

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return f(head)

