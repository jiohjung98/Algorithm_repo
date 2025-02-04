import sys
input = sys.stdin.readline

t = int(input())

def fibo(n):
    number = [[0,0] for _ in range(101)]
    number[0] = [1,0]
    number[1] = [0,1]

    for i in range(2,n+1):
        number[i][0] = number[i-1][0] + number[i-2][0]
        number[i][1] = number[i-1][1] + number[i-2][1]

    return number[n]

for _ in range(t):
    n = int(input())
    f = fibo(n)
    print(f[0], f[1])