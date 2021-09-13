from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    while not (n % 2):
        n //= 2
    if (n == 1):
        print(2)
        continue
    a = 3
    while (sqrt(n) >= a):
        while not (n % a):
            n //= a
        a += 2
    if (n > 2):
        print(n)
    else:
        print(a - 2)
