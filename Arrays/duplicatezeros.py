from typing import List


def duplicateZeros(arr:List[int]):
    i = 0
    while i<=len(arr)-1:
        if arr[i] == 0:
            arr.insert(i+1,0)
            del arr[len(arr) - 1]
            i+=2
        else:
            i+=1

def duplicateZeros2(arr:List[int]) -> None:
    result = []
    n = len(arr)

    for val in arr:
        result.append(val)

        if val == 0:
            result.append(val)

        if len(result) == n:
            break

    for i in range(n):
        arr[i] = result[i]


if __name__=="__main__":
       duplicateZeros([1,0,2,3,0,4,5,0]) 