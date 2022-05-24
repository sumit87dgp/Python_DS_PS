from collections import deque
from btree import TreeNode

def leastCommonAncestor(root:TreeNode, p: TreeNode, q: TreeNode) -> 'TreeNode':
    if root is None:
        return

    pArray = deque()
    qArray = deque()
          

