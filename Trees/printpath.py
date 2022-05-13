from array import array
from collections import deque
from multiprocessing.dummy import Array
from btree import TreeNode

def printBTreePath(root,nodepath,pathLen):
    if root is None:
        return

    #nodepath.insert(pathLen,root)    
    #nodepath[pathLen] = root
    nodepath[pathLen] = root.data
    pathLen +=1

    if root.left is None and root.right is None:
        print("\n")
        printpath(nodepath)
        #nodepath.pop()
       # del nodepath[pathLen]
    else:
        printBTreePath(root.left,nodepath, pathLen)
        printBTreePath(root.right, nodepath,pathLen)

def printpath(nodelist):
    for node in nodelist:
        print(node)         

def main():
    # root = TreeNode(989)
    # #root.left = TreeNode(2)
    # root.right = TreeNode(10250)
    # root.right.left = TreeNode(98693)
    # root.right.right = TreeNode(-89388)
    # root.right.right.right = TreeNode(-32127)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    
    path = deque()
    #path.in
    
    #path.
    #path.
    myarr = array('i',[10,9,8,90,12])
    printBTreePath(root,myarr,0)    


if __name__ == "__main__":
    main()
