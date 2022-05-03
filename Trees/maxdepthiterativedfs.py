# Program to find the maximum depth of the tree
# ========================================================================
# Technique : Iterative DFS using Stack
from btree import TreeNode


def maxDepth(root):
    if root is None:
        return 0

    mystack = [[root, 1]]
    res = 1
    while mystack:
        node, depth = mystack.pop()

        if node:
            res = max(res, depth)
            mystack.append([node.left, depth+1])
            mystack.append([node.right, depth+1])

    return res


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
