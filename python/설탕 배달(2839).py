# 방법 1 - 그리디
# N = int(input())
# cnt = 0

# while N >= 0:
#     if N % 5 == 0:
#         cnt += int(N//5)
#         print(cnt)
#         break
    
#     N -= 3
#     cnt += 1

# else:
#     print(-1)


# 방법 2 - DP
N = int(input())
dp = [float('inf')] * (N+1)
dp[0] = 0

for i in range(3, N+1):
    if i >= 3 and dp[i-3] != float('inf'):
        dp[i] = min(dp[i], dp[i-3]+1)
    if i >= 5 and dp[i-5] != float('inf'):
        dp[i] = min(dp[i], dp[i-5]+1)

print(dp[N] if dp[N] != float('inf') else -1)