from pip import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    maxval = 0
    count = 0
    for i in range(0,len(nums)):
        if nums[i] == 1:
            count += 1
        else:                
            maxval = max(count,maxval)
            count = 0
    #return maxval -- This is because the max value is not reassigned at the end of loop
    return max(count,maxval)  

if __name__ == "__main__":
    findMaxConsecutiveOnes([1,1,0,1,1,1])