

def find_largest_three(arr):
    if len(arr) < 3:
        return arr

    first = second = third = float('-inf')
    for i in range(len(arr)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]

    return [first, second, third]

#Example usecase
input_array = [12, 32, 45, 65, 78, 56, 34, 23]

largest_three = find_largest_three(input_array)

print(largest_three)