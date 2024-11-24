def rearrange_even_odd(arr):
    n = len(arr)

    # Sorting the array
    arr.sort()

    # Creating a temporary array to store rearranged elements
    temp = [0] * n

    # Fill even positions with larger elements
    even_index = n - 1
    for i in range(0, n, 2):
        temp[i] = arr[even_index]
        even_index -= 1

    # Fill odd positions with remaining elements
    odd_index = 0
    for i in range(1, n, 2):
        temp[i] = arr[odd_index]
        odd_index += 1

    # Copying the rearranged elements back to the original array
    for i in range(n):
        arr[i] = temp[i]

# Example usage
input_array = [1, 3, 2, 2, 5, 6, 7, 8]
rearrange_even_odd(input_array)
print("Rearranged array:", input_array)
