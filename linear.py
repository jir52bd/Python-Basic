#linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Example Usecase
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 12, 34]
target_number = int(input("Target :"))

index_linear = linear_search(numbers, target_number)

if index_linear != -1:
    print(f"Target {target_number} found at the index array[{index_linear}]")
else:
    print(f"Target {target_number} didn't found.")