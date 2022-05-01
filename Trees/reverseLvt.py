from btree import TreeNode
import collections

def reverseLvt(root):
    if root is None:
        return None

    mystack = collections.deque()
    myqueue = collections.deque()

    myqueue.append(root)

    while myqueue:
        currNode = myqueue.popleft()
        if currNode.left is not None:
            myqueue.append(currNode.left)

        if currNode.right is not None:
            myqueue.append(currNode.right)

        mystack.append(currNode)

    print("Reverse order lvt")

    

    while mystack:
        print(mystack.pop().data)               

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)

    reverseLvt(root)

if __name__=="__main__":
    main()