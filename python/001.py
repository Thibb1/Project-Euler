import sys
t = int(input())

def sumRange(x):
    return (x * (x + 1)) // 2

def sumDivisor(d, n):
    x = n // d
    x -= x * d >= n
    return d * sumRange(x)

for _ in range(t):
    n = int(input())
    a = sumDivisor(3, n)
    b = sumDivisor(5, n)
    c = sumDivisor(15, n)
    print(a + b - c)
