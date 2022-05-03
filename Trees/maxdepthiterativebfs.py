# Program to find the max depth of the tree
# =======================================================
# Technique : Iterative BFS using queue

from collections import deque
from itertools import count
from btree import TreeNode

def maxDepth(root):
    if root is None:
        return 0
    myqueue = deque([root])
    level = 0

    while myqueue:
        for i in range(len(myqueue)):
            node = myqueue.popleft()            
            if node.left:
                myqueue.append(node.left)
            
            if node.right:
                myqueue.append(node.right)
        level += 1

    return level    

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.left.left.right = TreeNode(11)

    print("The size of the tree is {}".format(maxDepth(root)))


if __name__ == "__main__":
    main()
