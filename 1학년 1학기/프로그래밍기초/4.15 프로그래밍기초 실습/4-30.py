def fastmult(m,n):
    def loop(m,n,ans):
        if n > 0:
            if n%2== 0:
                return loop(m+m,n//2,ans)
            else:
                return loop(m,n-1, ans + m)
        else:
            return ans
    return loop(m,n,0)

print(fastmult(10,64))
