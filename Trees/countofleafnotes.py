from btree import TreeNode

def countleafNote(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    totalleafnotes =  countleafNote(root.left) + countleafNote(root.right)

    return totalleafnotes

def main():
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(6)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(9)
    # root.left.left.right = TreeNode(11)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print("Total leaf notes in the tree is {}".format(countleafNote(root)))


if __name__ == "__main__":
    main()