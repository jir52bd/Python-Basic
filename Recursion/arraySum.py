
def sum_array(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n-1]+sum_array(arr, n-1)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_array(numbers, len(numbers)))