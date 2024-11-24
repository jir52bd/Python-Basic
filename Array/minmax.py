def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example array
array = [1, 2, 3, 4, 5]

# Call the function to reverse the array
reverse_array(array)

# Print the reversed array
print("Reversed Array:", array)
