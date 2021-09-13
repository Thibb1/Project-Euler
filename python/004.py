t = int(input())
a = []
for x in range(100, 1000):
    for y in range(100, 1000):
        p = x * y
        if str(p) == str(p)[::-1] and not p in a:
            a.append(p)
a = sorted(a)
for _ in range(t):
    n = int(input())
    x = 0
    while (x < len(a) and a[x + 1] < n):
        x += 1
    print(a[x])
