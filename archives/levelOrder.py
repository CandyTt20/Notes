class Tree(object):
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def levelOrder(self):
        #! 宽度遍历
        queue = [self]
        while queue:
            cur = queue.pop(0)
            print(cur._value,end=' ')
            if cur._left:
                queue.append(cur._left)
            if cur._right:
                queue.append(cur._right)
    
    def preOrder(self, root):
        #! 先序遍历
        #? 递归
        if root is None:
            return 
        print(root._value)
        self.preOrder(root._left)
        self.preOrder(root._right)


tree = Tree(1, Tree(2, Tree(4, Tree(8), None), Tree(5)),
            Tree(3, Tree(6), Tree(7)))
tree.preOrder(tree)
