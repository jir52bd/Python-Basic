

n, m = map(int, input().split())
v = [[] for _ in range(1000)]

for _ in range(m):
    x, y = map(int, input().split())
    v[x].append(y)
    v[y].append(x)

for i in range(1, n+1):
    print(i, end='')
    for j in v[i]:
        print('->', j, end='')
    print()

    