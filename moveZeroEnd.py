
def move_zero_end(arr):
    non_zero_count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_count] = arr[i]
            non_zero_count += 1

    while non_zero_count < len(arr):
        arr[non_zero_count] = 0
        non_zero_count += 1
    return arr

#user array
arr = [ 0, 2, 0, 3, 0, 4, 4, 0]

result_array = move_zero_end(arr)

print(result_array)