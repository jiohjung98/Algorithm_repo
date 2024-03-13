# 정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(num_list, n):
    answer = []
    for i in range(n-1, len(num_list)):
        answer.append(num_list[i])
    return answer

# 더 깔끔한 코드
# def solution(num_list, n):
#     answer = []
#     return num_list[n-1:]