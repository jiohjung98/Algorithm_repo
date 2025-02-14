# from collections import Counter

# n, taesu_score, p = map(int, input().split())
# if n > 0:   
#     score_arr = list(map(int, input().split()))
# else:
#     print(1)
#     exit(0)

# score_counter = Counter(score_arr)

# if n == p:
#     if taesu_score <= score_arr[-1]:
#         print(-1)
#     else:
#         score_arr.append(taesu_score)
#         score_arr.sort(reverse=True)
#         score_counter = Counter(score_arr)
#         score_data = sorted(score_counter.items(), key=lambda x:x[0], reverse=True)
#         # 태수 점수 위치 찾기
#         taesu_index = next(i for i, v in enumerate(score_data) if v[0] == taesu_score)
#         answer = 0 
#         for i in range(taesu_index):
#             answer += score_data[i][1]
#         print(answer+1)
# else:
#     score_arr.append(taesu_score)
#     score_arr.sort(reverse=True)
#     score_counter = Counter(score_arr)
#     score_data = sorted(score_counter.items(), key=lambda x:x[0], reverse=True)
#     # 태수 점수 위치 찾기
#     taesu_index = next(i for i, v in enumerate(score_data) if v[0] == taesu_score)
#     answer = 0 
#     for i in range(taesu_index):
#         answer += score_data[i][1]
#     print(answer+1)


n, score, p = map(int, input().split())

if n == 0:
  print(1)
else:
  rank = list(map(int, input().split()))

  if n == p and rank[-1] >= score:
    print(-1)
  else:
    result = n+1
    for i in range(n):
      if rank[i] <= score:
        result = i+1
        break
    print(result)