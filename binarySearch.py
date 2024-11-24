
def binary_search(arr, tar):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            left = mid+1
        else:
            right = mid-1

    return -1



#Example case
array_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
result = binary_search(array_list, target)
if result != -1:
    print(f"{target} is found at index array[{result}]")
else:
    print(f"{target} is not found.")