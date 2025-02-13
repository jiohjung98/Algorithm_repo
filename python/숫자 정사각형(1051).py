n, m = map(int, input().split())
arr = [
    list(map(int, input().strip()))
    for _ in range(n)
]

def find_square(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if arr[i][j] == arr[i+s-1][j] == arr[i+s-1][j+s-1] == arr[i][j+s-1]:
                return True
    return False

min_size = min(n,m)

for x in range(min_size, 0, -1):
    if find_square(x):
        print(x**2)
        break