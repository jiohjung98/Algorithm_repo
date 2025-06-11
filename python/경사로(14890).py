# 크기가 NxN인 지도, 각 칸 숫자는 높이값
# 2n만큼 길 존재
# 길 지나는 방법
# 1. 모든 길의 칸 높이가 같음
# 2. 경사로를 놓아서 지나는길 만들기
# -> 경사로 높이 : 1, 길이 L. 개수는 무제한

# 경사로 놓는 조건
# 1. 경사로는 낮은 칸에 놓고 L개의 연속된 칸에 경사로의 바닥이 모두 접해야 함
# 2. 낮은 칸과 높은 칸의 높이 차이는 1이어야 함
# 3. 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고 L개의 칸이 연속되어 있어야 함

import sys
input = sys.stdin.readline

N, L = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

def check(line, L):
    # 경사로 생기는 곳 체크하는 방문 배열
    visited = [False for _ in range(N)]
    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i] - line[i+1]) > 1:
            return False
        # 왼쪽이 더 클 때
        elif line[i] > line[i+1]:
            # temp 변수에 오른쪽 값 선언
            temp = line[i+1]
            for j in range(i+1, i+L+1):
                # 경사길이가 범위 내일 때
                if 0 <= j < N:
                    # 경사길이가 범위 내에서 다른 값을 가질 때
                    if temp != line[j]:
                        return False
                    # 높이는 같은데 이미 방문된 곳이면(경사로 놓은 곳)
                    elif visited[j]:
                        return False
                    # 경사로 놓기
                    visited[j] = True
                else:
                    return False
        # 오른쪽이 더 클 때
        else:
            # temp 변수에 왼쪽 값 선언
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
    
answer = 0
for lst in arr:
    if check(lst, L):
        answer += 1

# # 전치 행렬 선언
reverse_arr = list(map(list,zip(*arr)))

for lst in reverse_arr:
    if check(lst, L):
        answer += 1

print(answer)