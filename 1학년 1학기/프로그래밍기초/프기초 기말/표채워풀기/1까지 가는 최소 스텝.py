def minsteps(n):
    memo = [0 for _ in range(n+1)]
    for i in range(2,n+1):
        steps = memo[i-1]
        if i % 2 == 0:
            steps = min(steps, memo[i//2])
        if i % 3 == 0:
            steps = min(steps, memo[i//3])
        memo[i] = steps + 1
    return memo[n]