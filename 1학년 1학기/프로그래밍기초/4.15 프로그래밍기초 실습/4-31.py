def fastmult(m,n):
    ans = 0
    while n > 0:
        if n % 2 ==0:
            m,n = m+m, n //2
        else:
            n, ans = n -1 , ans+m


    return ans

print(fastmult(10,64))
print(fastmult(7,5))