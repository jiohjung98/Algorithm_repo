# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    answer = 0
    multiple = 1
    addAndsquare = 0
    for i in range(0, len(num_list)):
        multiple *= num_list[i]
        addAndsquare += num_list[i]
    addAndsquare *= addAndsquare
    if (multiple < addAndsquare):
        answer = 1
    else:
        answer = 0
    print(multiple, addAndsquare)
    return answer

# 더 깔끔한 코드
# def solution(num_list):
#     mul = 1 
#     for n in num_list:
#         mul *= n
#     return int(mul < sum(num_list) ** 2)