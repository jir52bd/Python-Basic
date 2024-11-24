
def longest_common_prefix(strs):
    if not strs:
        return
    #shotest common string
    sortest_string = min(strs, key=len)
    #return sortest_string

    #Iterate the string
    for i, char in enumerate(sortest_string):
        for other in strs:
            if other[i] != char:
                return sortest_string[:i]

    return sortest_string




#example case
input_string = ['fruits','fruites','frupbe', 'frureat']

result = longest_common_prefix(input_string)

print(f"Longest common prefix: {result}")