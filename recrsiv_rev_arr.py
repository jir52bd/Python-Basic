#Reverse an array elements using Recursive Function

def recursive_fun(arr, start, end):

    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    return recursive_fun(arr, start+1, end-1)

#examle case
arr_element = [1, 2, 3, 4, 5, 6, 7, 8, 9]

start = 0
end = len(arr_element) -1
recur = recursive_fun(arr_element, start, end)
print(arr_element)
