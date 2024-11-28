# n = int(input())
# arr = [str(input()) for _ in range(n)]
# arr_dict = {}
# answer = []
# for a in arr:
#     if a.split()[0] in arr_dict:
#         arr_dict[a.split()[0]] += (a.split()[1])
#     else:
#         arr_dict[a.split()[0]] = a.split()[1]

# for k, v in arr_dict.items():
#     if len(v) == 5:
#         answer.append(k)
# answer.sort(reverse=True)
# for i in range(len(answer)):
#     print(answer[i])

n = int(input())
person_dict = {}

for _ in range(n):
    a, b = input().split()
    if b == 'enter':
        person_dict[a] = b
    else:
       del person_dict[a]
person_dict = sorted(person_dict.keys(), reverse=True)
for p in person_dict:
    print(p)