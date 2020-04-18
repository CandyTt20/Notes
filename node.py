class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Singlelist(object):
    def __init__(self, node=None):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count = count + 1
            cur = cur.next
        return count

    def append(self, item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self.__head
        while cur != None:
            print(str(cur.elem)+'->', end=" ")
            cur = cur.next


if __name__ == "__main__":
    ll = Singlelist()
    print(ll.is_empty())
    print("*" * 15)
    ll.append(12)
    ll.append(15)
    ll.append(23)
    print(ll.is_empty())
    print("*" * 15)
    ll.travel()
    print("*" * 15)
    print(ll.length())
