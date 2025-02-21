import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
temp = [0] * n

for i in range(n):
    cnt = 0 # 자신의 왼쪽에 키 큰 사람의 수

    for j in range(n):
        # 자신의 왼쪽에 키 큰 사람의 수가 맞고 그 자리에 아무도 없다면
        if cnt == m[i] and temp[j] == 0:
            temp[j] = i + 1
            break

        # 자리에 아무도 없다면 자신의 왼쪽에 키 큰 사람의 수를 카운트
        elif temp[j] == 0:
            cnt += 1

print(*temp)