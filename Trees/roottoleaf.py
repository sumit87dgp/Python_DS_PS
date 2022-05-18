from collections import deque
import collections
from btree import TreeNode


    
        

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.left.left.right = TreeNode(11)

    storageArray = [None] * 256
    pathLen = 0
    
    def root_to_leaf(node,storageRef,pathLen):
        
        if node is None:
            return

        storageRef[pathLen] = node
        pathLen += 1

        if node.right is None and node.left is None:
            printArrayElements(storageRef,pathLen)
        else:    
            root_to_leaf(node.left,storageRef,pathLen)
            root_to_leaf(node.right,storageRef,pathLen)
        

    root_to_leaf(root,storageArray,pathLen)

def printArrayElements(arraystorage,pathLen):
    for i in range(pathLen) :
        print(arraystorage[i].data)
    print("\n")    

if __name__=="__main__":
    main()