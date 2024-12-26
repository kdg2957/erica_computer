# 표채워풀기 버전
def minbags(n):
    table = [0,0,1,1,2,1,2] # 0 <= n <= 6
    for i in range(7,n+1):
        smallest = min(table[i-2], table[i-3], table[i-5])
        table.append(smallest + 1)
    return table[n]