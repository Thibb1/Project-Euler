t = int(input())
for _ in range(t):
    n = int(input())
    for x in range(n, 2**40, n):
        d = False
        for m in range(1, n + 1):
            if (x % m):
                d = True
                break
        if d:
            continue
        print(x)
        break
