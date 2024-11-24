#Decimal number to Roamn number

def decimal_to_roman(dn):
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    value = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
   # print(len(value))
    roman = ""
    for i in range(len(number)):
        while dn >= number[i]:
            dn -= number[i]
            # print(dn)
            roman += value[i]
            # print(roman)

    return roman


#usne case
decimal_number = int(input(": "))
roman_number = decimal_to_roman(decimal_number)
print(f"{decimal_number} : {roman_number}")