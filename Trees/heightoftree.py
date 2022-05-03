from btree import TreeNode


def heightofTree(root):
    if root is None:
        return 0
    leftHeight = heightofTree(root.left)
    rightHeight = heightofTree(root.right)
    return max(leftHeight, rightHeight) + 1
    #return leftHeight+1 if (leftHeight > rightHeight) else rightHeight+1


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.left.left.right = TreeNode(11)

    print("The size of the tree is {}".format(heightofTree(root)))


if __name__ == "__main__":
    main()
