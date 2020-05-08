class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    cur,length = slow,1
    while cur.next != slow:
        cur = cur.next
        length += 1
    return length

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print(cycle_length(head))

if __name__ == "__main__":
    main()