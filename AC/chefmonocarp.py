t = int(input())

for case in range(t):
    n = int(input())
    t = list(map(int, input().split()))

    t = sorted(t)

    dp = [[0 for i in range(2*n + 1)] for j in range(n+1)]

    for i in range(n):
        dp[i][2*n] = 100000

    for j in reversed(range(2*n)):
        for i in reversed(range(n)):
            opt1 = dp[i][j+1]
            opt2 = dp[i+1][j+1] + abs(j - t[i])
            dp[i][j] = min(opt1, opt2)

    print(dp[0][1])
