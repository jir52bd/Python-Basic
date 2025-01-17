#Write a program to reverse an array or string

def reversed_array(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

#Example case
numbers = [1, 2, 3, 4, 5, 6,7,8]
print(numbers)
rev_numbers = reversed_array(numbers)
print(rev_numbers)