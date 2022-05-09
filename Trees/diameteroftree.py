from btree import TreeNode


# Diameter of Binary tree. Modified version of Height




def diabtree(root):
    if root is None:
        return 0
    lh = diabtree(root.left)
    rh = diabtree(root.right)

    ans = max(ans, 1+lh+rh)

    return max(lh, rh)+1


def heightoftree(root):
    if root is None:
        return 0

    lh = heightoftree(root.left)
    rh = heightoftree(root.right)
    return max(lh, rh)+1


def diamteroftree(root):
    if root is None:
        return 0

    dl = diamteroftree(root.left)
    dr = diamteroftree(root.right)

    curr = heightoftree(root.left) + heightoftree(root.right) + 1

    return max(curr, max(dl, dr))


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.left.left.right = TreeNode(11)

    global ans
    ans = 0
    # Time complexity O(n*2)
    print("Diameter of the tree {}".format(diamteroftree(root)))

    # Time complexity O(n)
    diabtree(root)
    #print("Diameter of the binary tree following O(n) is {}".format(ans))

if __name__ == "__main__":
    main()
