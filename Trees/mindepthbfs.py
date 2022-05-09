from collections import deque
from itertools import count
from platform import node
from btree import TreeNode

def mindepth(root):
    if root is None:
        return 0
    
    queue = deque([root])
    count = 1
    
    while queue:
        for i in range(len(queue)):
            currNode = queue.popleft()
            # This means this is the leaf node of the tree
            if currNode.left is None and currNode.right is None:
                return count
            
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
                
        count +=1

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    #root.left.left.right = TreeNode(11)

    print("The size of the tree is {}".format(mindepth(root)))


if __name__ == "__main__":
    main()
