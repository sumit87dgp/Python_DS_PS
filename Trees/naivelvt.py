class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = self.left = None


def PrintCurrentLevel(root, level):
    if root is None:
        return

    if level == 1:
        print(root.val)
    elif level > 1:
        PrintCurrentLevel(root.left, level-1)
        PrintCurrentLevel(root.right, level-1)


def main():    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)

    # Check if algorthim works

    for i in range(1, 4):        
        PrintCurrentLevel(root, i)


if __name__ == "__main__":
    main()
