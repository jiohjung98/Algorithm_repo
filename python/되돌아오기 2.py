# L - 왼쪽
# R - 오른쪽

# F - 이동

# 처음에 위를 보고 시작 

# 위를 보고 있을 때
# - L : 왼쪽(x-1)
# - R: 오른쪽(x+1)

# 오른쪽을 보고 있을 때
# - L : 위(y+1)
# - R : 아래(y-1)

# 아래를 보고 있을 때
# - L : 오른쪽(x+1)
# - R : 왼쪽(x-1)

# 왼쪽을 보고 있을 때
# - L : 아래(y-1)
# - R: 위(y+1)

arr = list(input())
start_x, start_y = 0,0

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

start_dir = mapper['N']

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0

for a in arr:
    if a == 'F':
        nx, ny = dxs[start_dir], dys[start_dir]
        # 0, 1
        start_x += nx
        start_y += ny
        cnt += 1
        nx, ny = 0, 0
        if start_x == 0 and start_y == 0:
            print(cnt)
            break
    elif a == 'L':
        if start_dir == 0:
            start_dir = mapper['W']
            cnt += 1
        elif start_dir == 1:
            start_dir = mapper['N']
            cnt += 1
        elif start_dir == 2:
            start_dir = mapper['E']
            cnt += 1
        else:
            start_dir = mapper['S']
            cnt += 1
    else:
        if start_dir == 0:
            start_dir = mapper['E']
            cnt += 1
        elif start_dir == 1:
            start_dir = mapper['S']
            cnt += 1
        elif start_dir == 2:
            start_dir = mapper['W']
            cnt += 1
        else:
            start_dir = mapper['N']
            cnt += 1

    

print(cnt)