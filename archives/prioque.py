class PrioQue(object):
    #! 线性表实现
    
    def __init__(self, elist=[]):
        self._elist = list(elist)
        self._elist.sort(reverse=True)

    def insert_que(self, elem):
        i = len(self._elist) - 1
        while i >= 0 and self._elist[i] < elem:
            i -= 1
        self._elist.insert(i + 1, elem)

    def is_empty(self):
        if len(self._elist) > 0:
            return False
        else:
            return True

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self._elist[len(self._elist)-1]

    def pop_que(self):
        if self.is_empty():
            return None
        else:
            return self._elist.pop()
x = PrioQue([5, 1, 2, 6, 3])
x.insert_que(4)
while x._elist:
    print(x.pop_que())
    print(x._elist)
