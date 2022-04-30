# importing the Class
from btree import TreeNode

from lvt import levelOrderTraversal


import collections

# function to insert Node
def insertNode(root, value):    
    if root is None:
        root = TreeNode(value)        
        return root

    myqueue = collections.deque()
    myqueue.append(root)

    while myqueue:
        currNode = myqueue.popleft()
        if currNode is not None:
            if currNode.left is not None:
                myqueue.append(currNode.left)
            else:
                currNode.left = TreeNode(value)
                return root  

        if currNode.right is not None:
            myqueue.append(currNode.right)
        else:
            currNode.right = TreeNode(value)
            return root

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    # root = None
    print(levelOrderTraversal(root))
    print("Inserting node now")
    print(levelOrderTraversal(insertNode(root,10)))
    #print(insertNode(root,10))
    # levelOrderTraversal(root)



if __name__ == "__main__":
    main();