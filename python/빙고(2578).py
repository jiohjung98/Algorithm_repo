import sys
input = sys.stdin.readline

bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

bingo_num = []
for _ in range(5):
    bingo_num.append(list(map(int, input().split())))

def check():
    result = 0
    # 가로 빙고 체크
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j] == 0:
                cnt += 1
        if cnt == 5:
            result += 1
    
    # 세로 빙고 체크
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt += 1
        if cnt == 5:
            result += 1
    
    # 대각선 빙고 체크(왼->오)
    cnt = 0
    for i in range(5):
        if bingo[i][i] == 0:
            cnt += 1
    if cnt == 5:
        result += 1
    
    # 대각선 빙고 체크(오->왼)
    cnt = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            cnt += 1
    if cnt == 5:
        result += 1
    
    return result

def simulate():
    cnt = 0
    result = 0
    for i in range(5):
        for j in range(5):
            num = bingo_num[i][j]
            cnt += 1
            for x in range(5):
                for y in range(5):
                    if bingo[x][y] == num:
                        bingo[x][y] = 0
            result = check()
            if result >= 3:
                return cnt

print(simulate())