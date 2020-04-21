class Stack(object):
    # ? Stack堆栈，用顺序表（list）实现
    def __init__(self):
        self.__list = []

    def push(self, itme):
        self.__list.append(itme)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.peek())
print(s.peek())
