
def main():
    n = int(input())
    num = []

    for _ in range(n):
        num.append(input())

    num.sort()
    com = num[0]
    i = 1
    count = 1

    while True:
        if i == n:
            break
        if num[i] == com:
            count += 1
            i += 1
        else:
            print(f"{com} aparece {count} vez(es)")
            com = num[i]
            count = 0

    return 0


if __name__ == '__main__':
    main()