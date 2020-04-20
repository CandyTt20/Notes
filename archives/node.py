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

    def add(self, item):
        #! 头部插入节点
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        #! 尾部插入
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        #! 指定位置插入
        node = Node(item)
        pre = self.__head
        count = 0
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            while count < pos-1:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def travel(self):
        cur = self.__head
        while cur != None:
            print(str(cur.elem), end=" ")
            cur = cur.next
        print("")

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self.__head
        pre = None

        while cur != None:

            if cur.elem == item:
                if pre == None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    ll = Singlelist()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.travel()
    print('--'*10)
    ll.add(13)
    ll.travel()
    print('--'*10)
    ll.add(14)
    ll.travel()
    print('--' * 10)
    ll.insert(6, 40)
    ll.travel()
    ll.remove(14)
    ll.travel()
    print(ll)
