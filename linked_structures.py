from single_linkedlist import ListNode


def insafter(head, x, val):
    res = head.search(x)
    if res[0] == True:
        res[2].insert(val)


def insbefore(head, x, val):
    res = head.search(x)
    if res[0] == True:
        if res[2] is head:
            new = ListNode(val)
            new.next = head
            head = new
        else:
            res[1].insert(val)
    return head
def delnode(head,x):
    res=head.search(x)
    if res[0]==True:
        if res[2] is head:
            head=head.next
        else:
            res[1].delete()
    return head
def buildlist(val):
    assert len(val)>0,"no elements"
    a=ListNode(val[0])
    b=a
    for i in range(1,len(val),1):
        b.insert(val[i])
        b=b.next
    return a
def instail(h,x):
    if h is None:
        return ListNode(x)
    a=h
    while a.next is not None:
        a=a.next
    new=ListNode(x)
    a.next=new
    return h
# n=ListNode(8)
# insafter(n,8,9)
# n.traverse()