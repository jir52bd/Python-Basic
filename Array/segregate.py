
def lomuto_partition(arr):
    pivot = arr[-1] #chose the pivot(last element)

    #initilization an index to track the position for the even number
    even_index = 0
    n = len(arr)
    for i in range(n):
        if arr[i] % 2 == 0: #If even
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1

    #swap the pivot element to its final position
    arr[even_index], arr[-1] = arr[-1], arr[even_index]

#use cade
numbers = [5, 8, 12, 7, 10, 3, 6]

lomuto_partition(numbers)

print(numbers)