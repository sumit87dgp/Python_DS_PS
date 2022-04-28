# To import queue datastructure
from ast import Not
import collections
from logging import root


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None


def findelementinTree(root, searchElement):
    elementFound = False
    if root == None:
        print("Tree is Empty")
        return
    myqueue = collections.deque()
    myqueue.append(root)
    while myqueue:
        currNode = myqueue.popleft()
        if currNode.data == searchElement:
            elementFound = True
            break
        if currNode.left is not None:
            myqueue.append(currNode.left)
        
        if currNode.right is not None:
            myqueue.append(currNode.right)

    if elementFound:
        print("The searched element {} is found".format(searchElement))
    else:
        print("The searched element {} is not found".format(searchElement))

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    # root = None
    findelementinTree(root,10)


if __name__ == "__main__":
    main()    