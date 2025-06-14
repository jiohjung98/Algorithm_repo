import sys
input = sys.stdin.readline


def row(a,n):
    for i in range(9):
        if n == sudoku[a][i]:
            return False
    return True

def col(a,n):
    for i in range(9):
        if n == sudoku[i][a]:
            return False
    return True

def square(y,x,n):
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3 * 3 + i][x//3 * 3 + j]:
                return False
    return True

def find(n):
    if n == len(blank):
        for s in sudoku:
            print(''.join(map(str, s)))
        exit()
    
    y = blank[n][0]
    x = blank[n][1]
    for i in range(1,10):
        if row(y,i) and col(x,i) and square(y,x,i):
            sudoku[y][x] = i
            find(n+1)
            sudoku[y][x] = 0

sudoku = [
    list(map(int, input().strip()))
    for _ in range(9)
]

blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])

find(0)