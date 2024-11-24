#Python Program to Find the Square Root
def square_root(num, epsilon = 1e-6):
    if num < 0:
        raise ValueError

    guess = num
    prev_guess = 0
    while abs(guess - prev_guess) > epsilon:
        prev_guess = guess
        guess = 0.5 *(guess+num/guess)

    return guess


#Example case
number = float(input())

sqrt = square_root(number)

print(sqrt)

# num = 25
#
# sqt_num = num ** 0.5
#
# print(sqt_num)