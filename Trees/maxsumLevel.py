from typing import Optional
from btree import TreeNode
from collections import deque

def maxLevelSum(root: Optional[TreeNode]) -> int:
    q = deque([root])
    maxsum = root.data
    level = 1
    maxSumLvl = 1
    while q:
        currSum = 0
        for i in range(len(q)):
            tmpNode = q.popleft()
            currSum+=tmpNode.data
            
            if tmpNode.left is not None:
                q.append(tmpNode.left)
            
            if tmpNode.right is not None:
                q.append(tmpNode.right)                    
        
        
        if (currSum > maxsum):
            maxsum = currSum
            maxSumLvl = level
        
        level += 1
        
    return maxSumLvl

def main():
    root = TreeNode(989)
    #root.left = TreeNode(2)
    root.right = TreeNode(10250)
    root.right.left = TreeNode(98693)
    root.right.right = TreeNode(-89388)
    root.right.right.right = TreeNode(-32127)

    print("The max sum level is at {}".format(maxLevelSum(root)))


if __name__ == "__main__":
    main()