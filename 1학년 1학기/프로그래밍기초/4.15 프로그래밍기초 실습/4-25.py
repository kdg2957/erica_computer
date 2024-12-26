def even(n):
    return n % 2 == 0

def odd(n):
    return n % 2 == 1

def gcd(m,n):
    k = 1
    while not (m == 0 or n == 0):
        if even(m) and even(n):
            m, n, k = m//2, n//2, k * 2 
        elif even(m) and odd(n):
            m = m//2 
        elif odd(m) and even(n):
            n = n//2
        elif m <= n:
            n = (n-m)//2
        else:
            m, n = n, (m-n)//2
    if m == 0:
        return n*k
    else: # n == 0
        return m*k
    
    
    
print(gcd(48,18))  # 6
print(gcd(18,48))  # 6
print(gcd(192,72)) # 24
print(gcd(18,57))  # 3
print(gcd(0,11))   # 11