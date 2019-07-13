# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        aux = []
        while head != None:
            aux.append(head.val)
            head = head.next
        aux.reverse()
        temp = head = ListNode(aux[0])
        aux.pop(0)
        for el in aux:
            otracosa = ListNode(el)
            temp.next = otracosa
            temp = otracosa
        return head

