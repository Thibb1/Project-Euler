t = int(input())
for _ in range(t):
    n = int(input())
    a = 0
    b = 2
    s = 0
    while (n >= b):
        s += b
        a, b = b, b * 4 + a 
    print(s)
