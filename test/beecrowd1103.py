
#use case
while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    if h1 == 0:
        hour1 = 24 * 60 + m1
    else:
        hour1 = h1 * 60 + m1
    if h2 == 0:
        hour2 = 24 * 60 + m2
    else:
        hour2 = h2 * 60 + m2

    if hour2 > hour1:
         print(hour2 - hour1)
    else:
        print(24 * 60 - (hour1 - hour2))
