class Tree(object):
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def levelOrder(self):
        queue = [self]
        while queue:
            cur = queue.pop(0)
            print(cur._value,end=' ')
            if cur._left:
                queue.append(cur._left)
            if cur._right:
                queue.append(cur._right)


tree = Tree(1, Tree(2, Tree(4, Tree(8), None), Tree(5)),
            Tree(3, Tree(6), Tree(7)))
tree.levelOrder()
