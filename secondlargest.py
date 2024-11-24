

def find_large_two(array):
    if len(array) < 2:
        return Exception

    fist_max = second_max = float('-inf')

    for i in range(len(array)):
        if array[i] > fist_max:
            second_max = fist_max
            fist_max = array[i]
        elif array[i] > second_max:
            second_max = array[i]

    return second_max

#Example case
n = int(input("Enter size of the array "))

arr = []

for i in range(n):
    element = int(input())
    arr.append(element)

large_two = find_large_two(arr)
# print(arr)
print(large_two)