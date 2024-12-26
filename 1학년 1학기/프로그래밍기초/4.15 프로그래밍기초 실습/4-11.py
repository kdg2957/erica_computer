def sumrange(m,n):
    def loop(m,total):
        if m <= n:
            return loop(m+1,m+total)
        else:
            return total
    return loop(m,0)


print(sumrange(3,2))
print(sumrange(3,3))
print(sumrange(3,4))
print(sumrange(3,6))
print(sumrange(1,10))
print(sumrange(-5,10))
