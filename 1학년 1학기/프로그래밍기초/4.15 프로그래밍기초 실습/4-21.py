def gcd(m,n):
    while n != 0:
        m , n = n , m%n
        

    return m


# Test code
print(gcd(48,18))  # 6
print(gcd(18,48))  # 6
print(gcd(192,72)) # 24
print(gcd(18,57))  # 3
print(gcd(0,11))   # 11