# 시간 초과
# import sys

# input = sys.stdin.readline()
# N = int(input)

# ans = 0
# for i in range(1, N+1):
#     ans += len(str(i))

# print(ans)

n = input()

comp = len(n)-1
ans = 0

for i in range(comp):
    ans += 9 * (10**i) * (i+1)

ans += (int(n)-(10**comp)+1) * (comp+1)

print(ans)