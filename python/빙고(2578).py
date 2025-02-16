def check():
    result = 0
    # 각 행에서 탐색 
    for i in range(5):
        count = 0
        for j in range(5):
            if myBingo[i][j] == 0: 
                count += 1
        if count == 5:
            result += 1
    
    for j in range(5):
        count = 0
        for i in range(5):
            if myBingo[i][j] == 0:
                count += 1
        if count == 5: 
            result += 1
    
    count = 0
    for i in range(5):
        if myBingo[i][i] == 0:
            count += 1
    if count == 5:
        result += 1

    count = 0
    for i in range(5):
        if myBingo[i][4 - i] == 0:
            count += 1
    if count == 5: 
        result += 1

    return result 

def simulate():
    count = 0
    result = 0
    for i in range(5):
        for j in range(5):
            x = bingoNum[i][j]
            count += 1        
            for a in range(5):
                for b in range(5):
                    if myBingo[a][b] == x:
                        myBingo[a][b] = 0 
            result = check() 
            if result >= 3: 
                return count

myBingo = []
for _ in range(5):
    myBingo.append(list(map(int,input().split())))

bingoNum = []
for _ in range(5):
    bingoNum.append(list(map(int,input().split())))

print(simulate())