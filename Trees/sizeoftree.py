from btree import TreeNode


def sizeofTree(node):
    countleft = 0 if node.left is None else sizeofTree(node.left)
    countright = 0 if node.right is None else sizeofTree(node.right)
    return 1 + countleft + countright

def sizeofTree2(node):
    if node is None:
        return 0
    
    if node.left is None and node.right is None:
        return 1
    else:
        return 1 + sizeofTree2(node.left) + sizeofTree2(node.right)

def main():
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(6)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(9)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.left.left.right = TreeNode(11)

    print("The size of the tree is {}".format(sizeofTree(root)))

    print("The size of the tree is {}".format(sizeofTree2(root)))


if __name__ == "__main__":
    main()
