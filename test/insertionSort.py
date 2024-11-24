

def insertion_sort(arr):
    tem = 0
    n = len(arr)
    #chacking odd position and assending order
    for i in range(2, n, 2):
        tem = arr[i]
        j = i -2
        while j >= 0 and arr[j] < tem:
            arr[j+2] = arr[j]
            j -= 2
        arr[j+2] = tem
   # return arr
    #sort odd position element in assending order
    for i in range(1, n, 2):
        tem = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= tem:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tem
    return arr
#example case
example_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort = insertion_sort(example_arr)
print(insertion_sort)
