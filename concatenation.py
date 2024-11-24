
def concatenate_string(s1, s2):
    result = ""
    for ch1 in s1:
        result += ch1

    for ch2 in s2:
        result += ch2

    return result


#Example usecase
str1 = "Hello, "
str2 = "world!"

concatanated_string = concatenate_string(str1, str2)

print(concatanated_string)
