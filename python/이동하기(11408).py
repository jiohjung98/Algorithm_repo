n, m = map(int, input().split())
miro = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0] * m for _ in range(n)]

miro_reverse = list(row for row in zip(*miro))

dp[0][0] = miro[0][0]

for i in range(1, m):
    dp[0][i] = sum(miro[0][:i+1])

for j in range(1, n):
    dp[j][0] = sum(miro_reverse[0][:j+1])

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + miro[i][j]

print(dp[n-1][m-1])

