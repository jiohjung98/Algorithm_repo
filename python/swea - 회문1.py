# for i in range(1, 11):
#     n = int(input())
#     arr =[]
#     for _ in range(8):
#         a = list(input())
#         arr.append(a)
    
#     cnt = 0
#     half_num = n // 2

#     for j in range(8):
#         for jj in range(8-n+1):
#             tmp_arr = arr[j][jj:jj+n]
#             # 짝수
#             if n % 2 == 0:
#                 left_arr = tmp_arr[:half_num]
#                 right_arr = tmp_arr[half_num:n]
#             else:
#                 left_arr = tmp_arr[:half_num]
#                 right_arr = tmp_arr[half_num+1:n]
#             if left_arr == right_arr[::-1]:
#                 cnt += 1
    
#     for k in range(8):
#         for kk in range(8-n+1):
#             tmp_arr = []
#             for kkk in range(n):
#                 tmp_val = arr[kk+kkk][k]
#                 tmp_arr.append(tmp_val)
#             if n % 2 == 0:
#                 left_arr = tmp_arr[:half_num]
#                 right_arr = tmp_arr[half_num:n]
#             else:
#                 left_arr = tmp_arr[:half_num]
#                 right_arr = tmp_arr[half_num+1:n]
#             if left_arr == right_arr[::-1]:
#                 cnt += 1

#     print('#'+ str(i), cnt)
        

# 개선 코드

for tc in range(1, 11):
    n = int(input())
    arr = []
    for _ in range(8):
        a = input()
        arr.append(list(a))
    
    arr2 = list(map(list, zip(*arr)))
    cnt = 0
    
    def is_palindrome(x):
        return x == x[::-1]
    
    for i in range(8):
        for j in range(8-n+1):
            if is_palindrome(arr[i][j:j+n]):
                cnt += 1
    for i in range(8):
        for j in range(8-n+1):
            if is_palindrome(arr2[i][j:j+n]):
                cnt += 1
                
    print(f'#{tc} {cnt}')