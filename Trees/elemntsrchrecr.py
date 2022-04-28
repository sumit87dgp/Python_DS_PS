from btree import TreeNode

def findelemeRecursive(root,ele):
    
    if root is None:
        return 0
    else:
        if root.data == ele:
            return 1
        else:
            temp = findelemeRecursive(root.left, ele)
            if temp != 0:
                return temp
            else:
                return findelemeRecursive(root.right,ele)
    


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(9)
    # root = None
    value =  findelemeRecursive(root,4)
    if value != 0:
        print("Element is found")
    else:
        print("Element not found")
            

if __name__ == "__main__":
    main()  