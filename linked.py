class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def prepend(head, val):
    newNode = ListNode(val)
    newNode.next = head
    head = newNode
    return head

def append(head, val):
    newNode = ListNode(val)
    newNode.next = head
    head = newNode
    tr = head
    while tr.next != None:
        tr = tr.next
    tr.next = head
    head.next = None

head = ListNode(5)
revhead = ListNode(5)
for i in range(5):
    head = prepend(head, i)
    append(revhead, i)
tr = head
while tr != None:
    print tr.val
    tr = tr.next
tr = revhead
while tr != None:
    print tr.val
    tr = tr.next
