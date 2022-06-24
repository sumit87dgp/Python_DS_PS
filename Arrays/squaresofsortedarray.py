
from collections import deque
from pip import List


def sortedSquares(nums: List[int]) -> List[int]:
    resultnums = deque([])
    i = 0
    j = len(nums) - 1
    while j >= i:
        if abs(nums[i]) > abs(nums[j]):
            resultnums.appendleft(nums[i] * nums[i])
            #nums[j] = nums[i] * nums[i]
            i+=1
        elif abs(nums[i]) < abs(nums[j]):
            resultnums.appendleft(nums[j] * nums[j])
            #nums[j] = nums[j] * nums[j]
            j -= 1
        else:
            resultnums.appendleft(nums[j] * nums[j])
            #nums[j] = nums[j] * nums[j]
            #i+=1
            j-=1
    
    return resultnums

if __name__ == "__main__":
    sortedSquares([-4,-1,0,3,10])