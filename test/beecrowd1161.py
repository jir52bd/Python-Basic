def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    try:
        m, n = map(int, input().split())
        if m == n == -1:
            break

        result = factorial(m) + factorial(n)
        print(result)
    except EOFError:
        break
