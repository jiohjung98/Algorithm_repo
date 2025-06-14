import sys
input = sys.stdin.readline

r,c,k = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(3)
]

def sorting(matrix, RC):
    sorted_matrix = []
    max_cnt = 0
    for i in range(len(matrix)):
        tmp_arr = []
        dic = dict()
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                if matrix[i][j] not in dic:
                    dic[matrix[i][j]] = 1
                else:
                    dic[matrix[i][j]] += 1
        
        for key, value in dic.items():
            # key : 숫자, value: 횟수 순차적으로 저장
            tmp_arr.append([key,value])
        # 횟수로 먼저 정렬, 이후 숫자로 정렬
        tmp_arr.sort(key = lambda x: [x[1], x[0]])
         # 2차원 배열 -> 1차원 배열 변환
        one_dimension_arr = sum(tmp_arr, [])
        max_cnt = max(max_cnt, len(one_dimension_arr))
        sorted_matrix.append(one_dimension_arr)
    
    for elem in sorted_matrix:
        # 최대로 긴 행의 길이 - 현재 행의 길이 만큼 0을 현재 행에 추가해주기
        elem += [0] * (max_cnt - len(elem))
        # 100 초과했으면
        if len(elem) > 100:
            elem = elem[:100]
    
    # RC = R이면 그대로 반환, C면 전치행렬로 변환 후 반환
    return sorted_matrix if RC == 'R' else list(zip(*sorted_matrix))

time = 0

while True:
    if time >= 101:
        time = -1
        break

    if r-1 < len(arr) and c-1 < len(arr[0]):
        if arr[r-1][c-1] == k:
            break
    # 행의 길이 >= 열의 길이이면
    if len(arr) >= len(arr[0]):
        arr = sorting(arr, 'R')
    else:
        # 전치행렬로 변환하고 진행
        arr = list(zip(*arr))
        arr = sorting(arr, 'C')
    time += 1

print(time)