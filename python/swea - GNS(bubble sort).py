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

    for i in range(leng-1):
        for j in range(i+1, leng):
            if mapper[arr[i]] > mapper[arr[j]]:
                arr[i], arr[j] = arr[j], arr[i]
    
    print(n)
    for elem in arr:
        print(elem ,end=' ')