"""
*
**
***
****
1
22
333
4444
55555
# """
# n = 4  # Number of rows
#
# for i in range(1, n + 1):
#     print('*' * i)
#Enter input
n = int(input('Enter the row of the pattern : '))

for i in range(1, n+1, 1):
    print(str(i)*i)

count = 0
for i in range(1,n+1):
    n = int(input())
    if n >= 50 and n <= 60:
        count = count+1

print(count)