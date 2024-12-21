arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

reversed_arr = list(map(list, zip(*arr)))

for i in range(19):
    for j in range(15):
        if arr[i][j:j+5] == [1,1,1,1,1]:
            print(1)
            print(i+1, j+3)
            exit()
        elif arr[i][j:j+5] == [2,2,2,2,2]:
            print(2)
            print(i+1, j+3)
            exit()

for i in range(19):
    for j in range(15):
        if reversed_arr[i][j:j+5] == [1,1,1,1,1]:
            print(1)
            print(j+3, i+1)
            exit()
        elif reversed_arr[i][j:j+5] == [2,2,2,2,2]:
            print(2)
            print(j+3, i+1)
            exit()

for i in range(14):
    for j in range(14):
        if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 1:
            print(1)
            print(i+3, j+3)
            exit()
        elif arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4] == 2:
            print(2)
            print(i+3, j+3)
            exit()

for i in range(18, 3, -1):
    for j in range(14):
        if arr[i][j] == arr[i-1][j+1] == arr[i-2][j+2] == arr[i-3][j+3] == arr[i-4][j+4] == 1:
            print(1)
            print(i-1, j+3)
            exit()
        elif arr[i][j] == arr[i-1][j+1] == arr[i-2][j+2] == arr[i-3][j+3] == arr[i-4][j+4] == 2:
            print(2)
            print(i-1, j+3)
            exit()

print(0)