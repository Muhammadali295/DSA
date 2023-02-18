from single_linkedlist import ListNode
from linked_structures import buildlist
def del_x(H, x):
    # see if any initial nodes contain x
    while H is not None and H.data == x:
        H =H.next
    # see if there IS a list left
    if H is None:
        return H
    a = H
    b = a.next
    while b is not None:
        if b.data == x:
            a.next = b.next
            b = a.next
        else:
            a = a.next
            b = b.next
    return H
# O(n)
# n=ListNode(8)
# n1=ListNode(9)
# n2=ListNode(10)
# n.next=n1
# n1.next=n2
#
# del_x(n,8)
# n.traverse()
def splitonneg(a):
    if a is None:  # no list
        return [None, None]
    # there is atleast one node
    q = a
    while q is not None:
        if q.data < 0:
            p = q.next
            q.next = None
            return [a, p]
        q = q.next
    return [a, None]
a=buildlist([1,2,3,-4,6,7])
print(a)
print(splitonneg(a))