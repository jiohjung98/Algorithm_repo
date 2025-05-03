# sugar = int(input())

# bag = 0
# while sugar >= 0:
#     if sugar % 5 == 0:
#         bag += (sugar // 5)
#         print(bag)
#         break
#     sugar -= 3
#     bag += 1
# else:
#     print(-1)

sugar = int(input())
dp = [float('inf')] * (sugar + 1)
dp[0] = 0

for i in range(3, sugar+1):
    if i >= 3 and dp[i-3] != float('inf'):
        dp[i] = min(dp[i], dp[i-3]+1)
    if i >= 5 and dp[i-5] != float('inf'):
        dp[i] = min(dp[i], dp[i-5]+1)

print(dp[sugar] if dp[sugar] != float('inf') else -1)
