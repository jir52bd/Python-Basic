

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr


#test case
ex_arr = [9, 13, 15, 11, 2]
selection_arr = selection_sort(ex_arr)
print(ex_arr)