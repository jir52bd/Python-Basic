

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr



#test case
ex_arr = [22, 14, 12, 18, 9]
bubble = bubble_sort(ex_arr)
print(bubble)