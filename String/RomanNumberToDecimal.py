#Roman Number to decimal number
def roman_to_decimal(rn):
    roman_matching = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    total = 0
    pre_value = 0
    for char in reversed(rn):
        value = roman_matching[char]
        if value >= pre_value:
            total += value
        else:
            total -= value
        pre_value = value

    return total

#Use Case
roman_number = input(": ")
decimal = roman_to_decimal(roman_number)

print(f"{roman_number} : {decimal}")