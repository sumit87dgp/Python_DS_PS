# To import queue datastrcuture
import collections

# Code to implement a binary tree


class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

# Function for level order traversal


def levelOrderTraversal(root):
    ans = []

    # Return null if the tree is empty
    if root is None:
        return ans

    # Initialize queue

    queue = collections.deque()
    queue.append(root)

    # Iterate over the queue until it's empty

    while queue:
        # Check the length of queue
        currSize = len(queue)
        currList = []

        while currSize > 0:
            # Dequeue element
            currNode = queue.popleft()
            currList.append(currNode.data)
            currSize -= 1

            # Check for left child
            if currNode.left is not None:
                queue.append(currNode.left)

            if currNode.right is not None:
                queue.append(currNode.right)

        ans.append(currList)

    return ans


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Check if the algorithm work
    print(levelOrderTraversal(root))


if __name__ == "__main__":
    main()
