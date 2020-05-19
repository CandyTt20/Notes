import heapq

class PrioQue(object):
    def __init__(self, elist=[]):
        self._elist = list(elist)
        self.build_heap()

    def build_heap(self):
        elist = self._elist
        index = len(elist) // 2 - 1
        for i in range(index, -1, -1):
            self.sift_down(elist, i)

    def sift_down(self, elist, pointer):
        child = 2 * pointer + 1

        while child < len(elist):
            if child +1 < len(elist) and elist[child] > elist[child + 1]:
                child += 1
            if elist[child] < elist[pointer]:
                elist[pointer], elist[child] = elist[child], elist[pointer]
                pointer = child
                child = 2*pointer+1
            else:
                break
    
    def sift_up(self, elist):
        pointer = len(elist) - 1
        father = (pointer-1)//2 #! 最后一个非叶子节点 index
        while pointer > 0:
            if elist[pointer] < elist[father]:
                elist[pointer], elist[father] = elist[father], elist[pointer]
                pointer = father
                father = (pointer - 1) // 2
            else:
                break

    def push(self, value):
        elist = self._elist
        elist.append(value)
        self.sift_up(elist)

    def pop(self):
        elist = self._elist
        if elist:
            elist[0], elist[-1] = elist[-1], elist[0]
            elist.pop()
            self.sift_down(elist,0)

l3=[]
l1= [1,5,6,4,7,9]
x = PrioQue(l3)
print(x._elist)
x.pop()
print(x._elist)

l2=[1,5,6,4,7,9]
heapq.heapify(l2)
heapq.heappop(l2)
print(l2)   


