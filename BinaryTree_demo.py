class Node:
    def __init__(self, data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    def preorder(self, start, tmp):
        if start is None:
            return
        tmp.append(start.data)
        self.preorder(start.left, tmp)
        self.preorder(start.right, tmp)
    def inorder(self, start, tmp):
        if start is None:
            return
        self.inorder(start.left, tmp)
        tmp.append(start.data)
        self.inorder(start.right, tmp)
    def postorder(self, start, tmp):
        if start is None:
            return
        self.postorder(start.left, tmp)
        self.postorder(start.right, tmp)
        tmp.append(start.data)
    def print_tree(self):
        tmp = []
        self.preorder(self.root, tmp)
        print('Preorder: ', end='')
        for i in tmp:
            print(i, end=' ')
        print()
        tmp = []
        self.inorder(self.root, tmp)
        print('Inorder: ', end='')
        for i in tmp:
            print(i, end=' ')
        print()
        tmp = []
        self.postorder(self.root, tmp)
        print('Postorder: ', end='')
        for i in tmp:
            print(i, end=' ')
        print()
