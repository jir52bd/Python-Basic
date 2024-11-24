

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#use case
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    result = gcd(n, m)
    print(result)
