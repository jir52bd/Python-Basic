
def is_armstrong(num):
    sum_n = 0
    n_str = str(num)
    power = len(n_str)
    n = int(num)
    while n > 0:
        digit = n % 10
        print("D -> ", digit)
        print("D*P -> ",digit**power)
        sum_n += digit ** power
        print("--", sum_n)
        n = n // 10
    return sum_n


#Input a number
number = int(input("Enter an integer number :"))

#check function to armstrong
arm_num = is_armstrong(number)

if arm_num == number:
    print(f"{number} is a armstrong number.")
else:
    print(f"{number} is not armstrong number")