mapper = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

T = int(input())

for tc in range(1, T+1):
    n, leng = tuple(map(str, input().split()))
    leng = int(leng)

    arr = list(map(str, input().split()))

    # 각 단어들의 개수를 담을 배열 선언
    cnt = [0] * 10 
    for i in range(leng):
        cnt[mapper[arr[i]]] += 1
    
    print(n)
    for elem in mapper:
        print((elem + ' ') * cnt[mapper[elem]], end=' ')