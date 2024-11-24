
def compute_length(word):
    count = 0
    for char in word:
        count += 1
    return count


user_input = input("Write a word: ")
length = compute_length(user_input)
print(length)

