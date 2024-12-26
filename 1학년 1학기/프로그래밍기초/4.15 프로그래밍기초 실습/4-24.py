def even(n):
    return n % 2 == 0

def odd(n):
    return n % 2 == 1

def gcd(m,n):
    def loop(m,n,k):
        if not (m == 0 or n == 0):
            if even(m) and even(n):
                return loop(m//2,n//2,k*2)
            elif even(m) and odd(n):
                return loop(m//2,n,k)
            elif odd(m) and even(n):
                return loop(m,n//2,k)
            elif m <= n:
                return loop(m,(n-m)//2,k)
            else:
                return loop(n,(m-n)//2,k)
        else:
            if m == 0:
                return n*k
            else: # n == 0
                return m*k
    return loop(m,n,1)

print(gcd(48,18))  # 6
print(gcd(18,48))  # 6
print(gcd(192,72)) # 24
print(gcd(18,57))  # 3
print(gcd(0,11))   # 11