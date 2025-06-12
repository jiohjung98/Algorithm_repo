import sys 
input = sys.stdin.readline

N, L = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

def check_lines(line, L):
    visited = [False for _ in range(N)]
    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i] - line[i+1]) > 1:
            return False
        # 왼쪽이 클 경우
        elif line[i] > line[i+1]:
            temp = line[i+1]
            for j in range(i+1, i+L+1):
                if 0 <= j < N:
                    if temp != line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
        # 오른쪽이 더 클 경우            
        else:
            temp = line[i]
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    if temp != line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
    return True

ans = 0
for line in arr:
    if check_lines(line, L):
        ans += 1

arr2 = list(map(list, zip(*arr)))
for line in arr2:
    if check_lines(line, L):
        ans += 1

print(ans)
 