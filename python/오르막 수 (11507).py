n = int(input())

dp = [1] * 10

for i in range(n):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(dp)