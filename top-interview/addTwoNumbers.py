# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        h = ListNode(None)
        c = h
        y = 0
        while c1!=None or c2!=None:
            a = c1.val if c1 else 0
            b = c2.val if c2 else 0
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
            cal = a + b + y
            if cal >= 10:
                y = cal//10
                cal = cal % 10
            else:
                y = 0
            node = ListNode(cal)
            c.next = node
            c = node
        if y != 0:
            node = ListNode(y)
            c.next = node
        return h.next

