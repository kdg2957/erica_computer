def mult(m,n):
    def loop(n,ans):
        if n > 0:
            return loop(n-1,ans+m)
        else:
            return ans
    return loop(n,0)

print(mult(4,6))
print(mult(7,5))