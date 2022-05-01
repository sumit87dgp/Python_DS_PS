from btree import TreeNode


def sizeofTree(node):
    countleft = 0 if node.left is None else sizeofTree(node.left)
    countright = 0 if node.right is None else sizeofTree(node.right)
    return 1 + countleft + countright


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)

    print("The size of the tree is {}".format(sizeofTree(root)))


if __name__ == "__main__":
    main()
