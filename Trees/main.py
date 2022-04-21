from logging import root
import btree


def findMax(root):

    # Base Case
    if (root == None):
        return float('-inf')
    
    # Return maximum of 3 values
    # 1) Root's data 2) Max in Left Subtree
    # 3) Max in Right Subtree

    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)

    if (lres > rres):
        res = lres
    if (rres > lres):
        res = rres
    return res

def main():
    print("main function is main.py is getting executed")
    root = btree.TreeNode(2)
    root.left = btree.TreeNode(7)
    root.right = btree.TreeNode(5)
    root.left.right = btree.TreeNode(6)
    root.left.right.left = btree.TreeNode(1)
    root.left.right.right = btree.TreeNode(11)
    root.right.right = btree.TreeNode(9)
    root.right.right.left = btree.TreeNode(4)

    print("Maximum element is", findMax(root))

    print("What does float('-inf prints')",float('-inf'))



if __name__ == "__main__":
    main()
else:
    print("kuch to garbar hain.")