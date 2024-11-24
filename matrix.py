#Largest element in the array

arr = [1, 3, 2, 5, 4, 8, 6, 9, 7]

check = 0

for i in range(1, len(arr)):
    if check <= arr[i]:
        check = arr[i]


print(check)
