from btree import TreeNode


def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.left.left.right = TreeNode(11)

    def mirror_tree(root):
        tmp = TreeNode()
        if root:
            mirror_tree(root.left)
            mirror_tree(root.right)

            tmp = root.left
            root.left = root.right
            root.right = tmp
        return root

    mirror_tree(root)      

if __name__ == "__main__":
    main()