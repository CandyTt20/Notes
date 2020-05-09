class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
    pre, cur = None, head
    while cur is not None:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre
        
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head=reverse(head)
    print(head.value)
    print(head.next.value)
main()