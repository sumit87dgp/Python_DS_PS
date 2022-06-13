from bstnode import BinarySearchTreeNode


def insertNode(root,val):
    if root is None:
        root = BinarySearchTreeNode(val)

    if val < root.data:
        insertNode(root.left,val)
    elif val > root.data:
        insertNode(root.right,val)            
    

    return root

def main():
    bstroot = BinarySearchTreeNode(6)
    bstroot.left = BinarySearchTreeNode(2)
    bstroot.right = BinarySearchTreeNode(8)
    pass

if __name__ == "__main__":
    main()