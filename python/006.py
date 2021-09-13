import sys
t = int(input())
def sumRange(x):
    return (x * (x + 1)) // 2
def sumRangePow(x):
    return (x * (x + 1) * (2 * x + 1)) // 6
for _ in range(t):
    n = int(input())
    a = sumRange(n)**2
    b = sumRangePow(n)
    print(a - b)
