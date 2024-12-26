def sumrange(m,n):
    total = 0
    while m <= n:
        total = total + m
        m = m + 1
    return total



print(sumrange(3,2))
print(sumrange(3,3))
print(sumrange(3,4))
print(sumrange(3,6))
print(sumrange(1,10))
print(sumrange(-5,10))