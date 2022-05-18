from btree import TreeNode

def root_to_leaf(node):
    if node is None:
        return

    root_to_leaf(node.left)
    root_to_leaf(node.right)
    print(node.data)
    
        

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    root.left.left.right = TreeNode(11)

    root_to_leaf(root)

if __name__=="__main__":
    main()