n = int(input())
dp = [[0] * 10 for _ in range(n+1)]

# 1의 자릿수의 경우의 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 가장 뒤 자리수가 0인 경우 - 앞에 1만 올 수 있음
# -> dp[자리수][0] = dp[자리수-1][1]

# 가장 뒤 자리수가 9인 경우 - 앞에 8만 올 수 있음
# -> dp[자리수][9] = dp[자리수-1][8]

# 가장 뒤 자리수가 x(1~8)인 경우 - 각각 2가지 경우가 올 수 있음
# -> dp[자리수][x] = dp[자리수-1][x-1] + dp[자리수-1][x+1]

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)