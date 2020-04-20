class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = []
        p2 = []

        while l1 != None:
            p1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            p2.append(l2.val)
            l2 = l2.next
        
        y = []
        temp = 0
        if len(p1) > len(p2):
            for i in range(len(p1) - len(p2)):
                p2.append(0)
        elif len(p2) > len(p1):
            for i in range(len(p2) - len(p1)):
                p1.append(0)

        for i in range(len(p1)):
            y.append((p1[i] + p2[i] + temp) % 10)
            if p1[i] + p2[i] + temp >= 10:
                temp = 1
            else:
                temp = 0
        if temp == 1:
            y.append(1)

        enter = ListNode(y[0])
        result = enter
        for i in range(len(y)-1):
            result.next = ListNode(y[i + 1])
            result = result.next

        return enter

def appendList(l):
    result = ListNode(l[0])
    head = result

    for i in range(len(l) - 1):
        head.next = ListNode(l[i + 1])
        head = head.next

    return result


def showList(head):
    l = []
    while head != None:
        l.append(head.val)
        head = head.next
    return l


x = appendList([2,4,3])
y = appendList([5,6,4])
z = Solution().addTwoNumbers(x, y)
print(showList(z))