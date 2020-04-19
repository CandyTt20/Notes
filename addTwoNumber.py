class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addList(l1, l2):
    result = []
    temp = 0
    if len(l1) > len(l2):
        for i in range(len(l1) - len(l2)):
            l2.append(0)
    elif len(l2) > len(l1):
        for i in range(len(l2) - len(l1)):
            l1.append(0)

    for i in range(len(l1)):
        result.append((l1[i] + l2[i] + temp) % 10)
        if l1[i] + l2[i] + temp >= 10:
            temp = 1
        else:
            temp = 0
    if temp == 1:
        result.append(1)
    return result


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
        result_p = addList(p1, p2)
        enter = ListNode(result_p[0])
        result = enter
        for i in range(len(result_p)-1):
            result.next = ListNode(result_p[i + 1])
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