def fastmult(m,n):
    if n > 0:
        if n % 2 == 0:
            return fastmult(m+m,n//2)
        else:
            return m+ fastmult(m,n-1)
    else:
        return 0
    
    
print(fastmult(10,64))
print(fastmult(7,5))